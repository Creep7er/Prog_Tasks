import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial import Delaunay

# ---------- MediaPipe ----------
mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

# ---------- Загрузка маски ----------
mask_img = cv2.imread("mask.png", cv2.IMREAD_UNCHANGED)

if mask_img is None:
    print("Ошибка: Не удалось загрузить mask.png")
    exit(1)

# Индексы ключевых точек для полного контура лица
FACE_OVERTURE = [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 
                 397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136,
                 172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109]

# Дополнительные точки для более точного контура
FULL_FACE_CONTOUR = FACE_OVERTURE + [195, 5, 4, 51, 52, 53, 286, 56, 57, 172, 136]

def create_face_mask(landmarks, frame_shape):
    """Создает маску лица на основе всех контурных точек"""
    h, w = frame_shape[:2]
    
    # Собираем все точки контура лица
    contour_points = []
    for idx in FULL_FACE_CONTOUR:
        x = int(landmarks[idx].x * w)
        y = int(landmarks[idx].y * h)
        contour_points.append([x, y])
    
    # Добавляем точки для шеи и подбородка для лучшего покрытия
    chin_points = [152, 148, 176, 149, 150, 136, 172, 58]
    for idx in chin_points:
        x = int(landmarks[idx].x * w)
        y = int(landmarks[idx].y * h) + int(h * 0.05)  # Немного расширяем вниз
        contour_points.append([x, y])
    
    # Преобразуем в numpy array
    contour_points = np.array(contour_points, dtype=np.int32)
    
    # Создаем маску лица
    face_mask = np.zeros((h, w), dtype=np.uint8)
    cv2.fillPoly(face_mask, [contour_points], 255)
    
    # Сглаживаем маску для более естественного перехода
    face_mask = cv2.GaussianBlur(face_mask, (5, 5), 0)
    
    return face_mask, contour_points

def warp_mask_to_face(mask, landmarks, frame_shape):
    """Деформирует маску под форму лица с помощью триангуляции"""
    h, w = frame_shape[:2]
    mh, mw = mask.shape[:2]
    
    # Выбираем ключевые точки на лице
    face_points = []
    mask_points = []
    
    # Соответствие между точками лица и маски
    point_mapping = [
        # Контур лица
        (10, [mw//2, 0]),  # Верх
        (152, [mw//2, mh-1]),  # Низ
        (234, [0, mh//2]),  # Лево
        (454, [mw-1, mh//2]),  # Право
        
        # Глаза
        (33, [int(mw*0.35), int(mh*0.3)]),  # Левый глаз
        (263, [int(mw*0.65), int(mh*0.3)]),  # Правый глаз
        
        # Нос
        (1, [mw//2, int(mh*0.5)]),  # Кончик носа
        (168, [mw//2, int(mh*0.4)]),  # Переносица
        
        # Рот
        (61, [int(mw*0.4), int(mh*0.6)]),  # Левый угол рта
        (291, [int(mw*0.6), int(mh*0.6)]),  # Правый угол рта
        (0, [mw//2, int(mh*0.55)]),  # Верхняя губа
        (17, [mw//2, int(mh*0.65)]),  # Нижняя губа
        
        # Брови
        (70, [int(mw*0.3), int(mh*0.2)]),  # Левая бровь
        (300, [int(mw*0.7), int(mh*0.2)]),  # Правая бровь
        
        # Скулы
        (116, [int(mw*0.25), int(mh*0.4)]),  # Левая скула
        (345, [int(mw*0.75), int(mh*0.4)]),  # Правая скула
    ]
    
    for face_idx, mask_pos in point_mapping:
        face_points.append([landmarks[face_idx].x * w, landmarks[face_idx].y * h])
        mask_points.append(mask_pos)
    
    # Добавляем дополнительные точки по краям для лучшей деформации
    edge_points = [
        (54, [int(mw*0.2), int(mh*0.8)]),   # Левая щека
        (284, [int(mw*0.8), int(mh*0.8)]),  # Правая щека
        (132, [int(mw*0.15), int(mh*0.5)]), # Левая сторона
        (361, [int(mw*0.85), int(mh*0.5)]), # Правая сторона
    ]
    
    for face_idx, mask_pos in edge_points:
        face_points.append([landmarks[face_idx].x * w, landmarks[face_idx].y * h])
        mask_points.append(mask_pos)
    
    # Добавляем угловые точки для стабильности
    face_points.append([0, 0])
    mask_points.append([0, 0])
    face_points.append([w, 0])
    mask_points.append([mw, 0])
    face_points.append([0, h])
    mask_points.append([0, mh])
    face_points.append([w, h])
    mask_points.append([mw, mh])
    
    face_points = np.array(face_points, dtype=np.float32)
    mask_points = np.array(mask_points, dtype=np.float32)
    
    # Создаем триангуляцию на маске
    try:
        tri = Delaunay(mask_points)
    except:
        # Если триангуляция не удалась, используем простое аффинное преобразование
        return simple_warp_mask(mask, landmarks, frame_shape)
    
    # Создаем деформированное изображение
    #warped_mask = np.zeros((h, w, 4), dtype=np.uint8)
    warped_mask = simple_warp_mask(mask_img, landmarks, frame.shape)
    # Для каждого треугольника выполняем аффинное преобразование
    for simplex in tri.simplices:
        # Получаем вершины треугольника на маске
        mask_tri = mask_points[simplex].astype(np.float32)
        
        # Получаем соответствующие вершины на лице
        face_tri = face_points[simplex].astype(np.float32)
        
        # Проверяем, что треугольник не вырожденный
        if np.linalg.det(np.column_stack([face_tri[1] - face_tri[0], 
                                          face_tri[2] - face_tri[0]])) < 1e-6:
            continue
            
        # Вычисляем ограничивающий прямоугольник для треугольника на лице
        face_rect = cv2.boundingRect(face_tri.astype(np.int32))
        face_rect = [max(0, face_rect[0]), max(0, face_rect[1]),
                     min(w - face_rect[0], face_rect[2]), 
                     min(h - face_rect[1], face_rect[3])]
        
        if face_rect[2] <= 0 or face_rect[3] <= 0:
            continue
        
        # Создаем маску для треугольника
        tri_mask = np.zeros((face_rect[3], face_rect[2]), dtype=np.uint8)
        
        # Смещаем координаты треугольника
        face_tri_shifted = face_tri - [face_rect[0], face_rect[1]]
        
        # Рисуем треугольник
        cv2.fillConvexPoly(tri_mask, face_tri_shifted.astype(np.int32), 255)
        
        # Смещаем координаты треугольника на маске
        mask_tri_shifted = mask_tri - [mw//2, mh//2]
        
        # Вычисляем матрицу аффинного преобразования
        try:
            # Преобразуем в правильный формат для getAffineTransform
            src_tri = np.array([mask_tri_shifted[0], mask_tri_shifted[1], mask_tri_shifted[2]], dtype=np.float32)
            dst_tri = np.array([face_tri_shifted[0], face_tri_shifted[1], face_tri_shifted[2]], dtype=np.float32)
            
            M = cv2.getAffineTransform(src_tri, dst_tri)
            
            # Применяем преобразование к треугольнику
            tri_warped = cv2.warpAffine(mask, M, (face_rect[2], face_rect[3]),
                                        flags=cv2.INTER_LINEAR,
                                        borderMode=cv2.BORDER_REFLECT)
            
            # Накладываем треугольник на итоговое изображение
            for c in range(4):
                warped_mask[face_rect[1]:face_rect[1]+face_rect[3],
                           face_rect[0]:face_rect[0]+face_rect[2], c] = \
                    cv2.bitwise_or(
                        warped_mask[face_rect[1]:face_rect[1]+face_rect[3],
                                   face_rect[0]:face_rect[0]+face_rect[2], c],
                        cv2.bitwise_and(tri_warped[:,:,c], tri_warped[:,:,c], mask=tri_mask)
                    )
        except:
            continue
    
    return warped_mask

def simple_warp_mask(mask, landmarks, frame_shape):
    """Простое аффинное преобразование маски (запасной вариант)"""
    h, w = frame_shape[:2]
    
    # Получаем ключевые точки лица
    left_eye = np.array([landmarks[33].x * w, landmarks[33].y * h])
    right_eye = np.array([landmarks[263].x * w, landmarks[263].y * h])
    nose = np.array([landmarks[1].x * w, landmarks[1].y * h])
    chin = np.array([landmarks[152].x * w, landmarks[152].y * h])
    
    # Вычисляем размеры лица
    face_width = abs(right_eye[0] - left_eye[0]) * 2.5
    face_height = abs(chin[1] - nose[1]) * 2.2
    
    # Масштабируем маску
    scale_x = face_width / mask.shape[1]
    scale_y = face_height / mask.shape[0]
    scale = max(scale_x, scale_y)
    
    new_width = int(mask.shape[1] * scale)
    new_height = int(mask.shape[0] * scale)
    
    mask_resized = cv2.resize(mask, (new_width, new_height))
    
    # Вычисляем позицию
    x_offset = int(nose[0] - new_width // 2)
    y_offset = int(nose[1] - new_height // 2)
    
    # Создаем пустое изображение
    warped_mask = np.zeros((h, w, 4), dtype=np.uint8)
    
    # Накладываем маску
    x1 = max(0, x_offset)
    y1 = max(0, y_offset)
    x2 = min(w, x_offset + new_width)
    y2 = min(h, y_offset + new_height)
    
    mask_x1 = max(0, -x_offset)
    mask_y1 = max(0, -y_offset)
    mask_x2 = mask_x1 + (x2 - x1)
    mask_y2 = mask_y1 + (y2 - y1)
    
    if x2 > x1 and y2 > y1:
        warped_mask[y1:y2, x1:x2] = mask_resized[mask_y1:mask_y2, mask_x1:mask_x2]
    
    return warped_mask

def realistic_blend(frame, mask, face_mask):
    """Реалистичное смешивание маски с лицом"""
    if mask.shape[2] == 4 and np.any(mask[:,:,3] > 0):
        # Нормализуем альфа-канал
        alpha = mask[:,:,3] / 255.0
        
        # Применяем маску лица
        face_mask_norm = face_mask / 255.0
        
        # Комбинируем альфа-каналы
        final_alpha = alpha * face_mask_norm
        
        # Ограничиваем альфа-канал
        final_alpha = np.clip(final_alpha, 0, 1)
        
        # Смешиваем
        for c in range(3):
            frame[:,:,c] = frame[:,:,c] * (1 - final_alpha) + mask[:,:,c] * final_alpha
        
        # Добавляем легкое размытие на границах
        frame = cv2.addWeighted(frame, 0.95, 
                                cv2.GaussianBlur(frame, (3, 3), 0), 0.05, 0)
    
    return frame

# ---------- Основной цикл ----------
cap = cv2.VideoCapture(0)

# Настройки для лучшего качества
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

with mp_face.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            
            # Создаем маску лица
            face_mask, face_contour = create_face_mask(landmarks, frame.shape)
            
            # Деформируем маску под лицо
            warped_mask = warp_mask_to_face(mask_img, landmarks, frame.shape)
            
            # Реалистично смешиваем
            frame = realistic_blend(frame, warped_mask, face_mask)

        cv2.imshow("Realistic Face Mask - Press ESC to exit", frame)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
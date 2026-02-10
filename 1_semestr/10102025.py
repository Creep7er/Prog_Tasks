import random

my_dict = {
    "document": {"uz": "hujjat", "trans": "[ˈdɒkjʊmənt]"},
    "tail": {"uz": "dum", "trans": "[teɪl]"},
    "bone": {"uz": "suyak", "trans": "[bəʊn]"},
    "father": {"uz": "ota", "trans": "[ˈfɑːðər]"},
    "job": {"uz": "ish, kasb", "trans": "[dʒɒb]"},
    "tree": {"uz": "daraxt", "trans": "[triː]"},
    "eye": {"uz": "ko‘z", "trans": "[aɪ]"},
    "color": {"uz": "rang", "trans": "[ˈkʌlər]"},
    "fruit": {"uz": "meva", "trans": "[fruːt]"},
    "key": {"uz": "kalit", "trans": "[kiː]"},
    "foot": {"uz": "oyoq", "trans": "[fʊt]"},
    "door": {"uz": "eshik", "trans": "[dɔːr]"},
    "school": {"uz": "maktab", "trans": "[skuːl]"},
    "hen": {"uz": "tovuq", "trans": "[hen]"},
    "teacher": {"uz": "o‘qituvchi", "trans": "[ˈtiːtʃər]"},
    "own": {"uz": "shaxsiy", "trans": "[əʊn]"},
    "baby": {"uz": "chaqaloq", "trans": "[ˈbeɪbi]"},
    "garden": {"uz": "bog‘", "trans": "[ˈɡɑːrdən]"},
    "eagle": {"uz": "burgut", "выход на однуtrans": "[ˈiːɡəl]"},
    "lady": {"uz": "xonim", "trans": "[ˈleɪdi]"},
    "girl": {"uz": "qiz bola", "trans": "[ɡɜːrl]"},
    "flat": {"uz": "kvartira", "trans": "[flæt]"},
    "boy": {"uz": "o‘gil bola", "trans": "[bɔɪ]"},
    "banana": {"uz": "banan", "trans": "[bəˈnɑːnə]"},
    "woman": {"uz": "ayol", "trans": "[ˈwʊmən]"},
    "daughter": {"uz": "qiz", "trans": "[ˈdɔːtər]"},
    "friend": {"uz": "do‘st", "trans": "[frend]"},
    "aunt": {"uz": "hola", "trans": "[ɑːnt]"},
    "son": {"uz": "o‘g‘il", "trans": "[sʌn]"},
    "husband": {"uz": "er", "trans": "[ˈhʌzbənd]"},
    "pen": {"uz": "ruchka", "trans": "[pen]"},
    "hoof": {"uz": "tuyoq", "trans": "[huːf]"},
    "nest": {"uz": "in, uya", "trans": "[nest]"},
    "forest": {"uz": "o‘rmon", "trans": "[ˈfɒrɪst]"},
    "river": {"uz": "daryo", "trans": "[ˈrɪvər]"},
    "year": {"uz": "yil", "trans": "[jɪr]"},
    "day": {"uz": "kun", "trans": "[deɪ]"},
    "company": {"uz": "kompaniya", "trans": "[ˈkʌmpəni]"},
    "hand": {"uz": "qo‘l", "trans": "[hænd]"},
    "place": {"uz": "joy", "trans": "[pleɪs]"},
    "problem": {"uz": "muammo", "trans": "[ˈprɒbləm]"},
    "child": {"uz": "bola", "trans": "[tʃaɪld]"},
    "number": {"uz": "son", "trans": "[ˈnʌmbər]"},
    "week": {"uz": "hafta", "trans": "[wiːk]"},
    "fact": {"uz": "dalil", "trans": "[fækt]"},
    "family": {"uz": "oila", "trans": "[ˈfæməli]"},
    "home": {"uz": "uy", "trans": "[hoʊm]"},
    "business": {"uz": "biznes", "trans": "[ˈbɪznəs]"},
    "country": {"uz": "mamlakat", "trans": "[ˈkʌntri]"},
    "meat": {"uz": "go‘sht", "trans": "[miːt]"},
    "meet": {"uz": "uchrashmoq", "trans": "[miːt]"},
    "ill": {"uz": "kasal", "trans": "[ɪl]"},
    "fill": {"uz": "to‘ldirmoq", "trans": "[fɪl]"},
    "fist": {"uz": "musht", "trans": "[fɪst]"},
    "list": {"uz": "ro‘yxat", "trans": "[lɪst]"},
    "far": {"uz": "uzoқ", "trans": "[fɑːr]"},
    "bar": {"uz": "mayxona", "trans": "[bɑːr]"},
    "but": {"uz": "biroq", "trans": "[bʌt]"},
    "nut": {"uz": "yong‘oq", "trans": "[nʌt]"},
    "sore": {"uz": "og‘riq", "trans": "[sɔːr]"},
    "pot": {"uz": "qozon", "trans": "[pɒt]"},
    "dot": {"uz": "nuqta", "trans": "[dɒt]"},
    "fog": {"uz": "tuman", "trans": "[fɒɡ]"},
    "food": {"uz": "ovqat", "trans": "[fuːd]"},
    "soup": {"uz": "sho‘rva", "trans": "[suːp]"},
    "moon": {"uz": "oy", "trans": "[muːn]"},
    "noon": {"uz": "tushlik vaqti", "trans": "[nuːn]"},
    "put": {"uz": "qo‘ymoq", "trans": "[pʊt]"},
    "full": {"uz": "to‘la", "trans": "[fʊl]"},
    "bull": {"uz": "buqa", "trans": "[bʊl]"},
    "net": {"uz": "tarmoq", "trans": "[net]"},
    "pet": {"uz": "uy hayvoni", "trans": "[pet]"},
    "set": {"uz": "joylamoq", "trans": "[set]"},
    "get": {"uz": "olmoq", "trans": "[ɡet]"},
    "turn": {"uz": "aylanmoq", "trans": "[tɜːn]"},
    "earn": {"uz": "pul ishlab topmoq", "trans": "[ɜːn]"},
    "burn": {"uz": "yonmoq", "trans": "[bɜːn]"},
    "along": {"uz": "bo‘ylab", "trans": "[əˈlɒŋ]"},
    "mad": {"uz": "jinni", "trans": "[mæd]"},
    "rat": {"uz": "kalamush", "trans": "[ræt]"}}


def huenction(my_dict):
    key = random.choice(list(my_dict.keys()))
    data = my_dict[key]

    direction = random.choice(["en_to_uz", "uz_to_en"])

    if direction == "en_to_uz":
        print(f"Английское слово: {key} {data['trans']}")
        answer = input("Переведи на узбекский: ").strip().lower()

        if answer == data["uz"].lower():
            print(" Правильно!\n")
            del my_dict[key]
        else:
            print(f" Неправильно. Правильный ответ: {data['uz']}\n")

    else:
        print(f"Узбекское слово: {data['uz']}")
        answer = input("Переведи на английский: ").strip().lower()

        if answer == key.lower():
            print(" Правильно!\n")
            del my_dict[key]
        else:
            print(f"Неправильно. Правильный ответ: {key}\n")


while my_dict:
    for _ in range(20):  
        if not my_dict:
            break
        huenction(my_dict)

    ans = input("Продолжить? (y/n): ").strip().lower()
    if ans != "y":
        print("Обучение завершено!")
        break

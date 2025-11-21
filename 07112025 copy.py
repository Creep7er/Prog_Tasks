import matplotlib.pyplot as plt

x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y1 = [i**2 for i in x]
y2 = [i**3 for i in x]

plt.plot(x, y1, label="x^2+2x+2", color='blue')
plt.plot(x, y2, label="x^3", color='red')

plt.legend()      # добавляем легенду
plt.title("Сравнение функций")
plt.show()

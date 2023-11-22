# Отрисовать с помощью Matplotlib изображение включающее в себя 2 трехмерных графика функции
# среднеквадратичного отклонения MSE. На втором графике ось z реализовать в логарифмическом масштабе.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Расчет значений MSE в логарифмическом масштабе
mse_values = np.log(Z)

# Построение первого графика
fig = plt.figure(figsize=(12, 6))

# График 1
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('График функции MSE')

# График 2
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, mse_values, cmap='viridis')

# Установка log масштаба по оси z
ax2.set_zscale('log')

# Уменьшение масштаба
ax2.set_box_aspect([1, 1, 0.25])

ax2.set_title('График функции MSE в Log масштабе')

# Отображение графиков
plt.show()




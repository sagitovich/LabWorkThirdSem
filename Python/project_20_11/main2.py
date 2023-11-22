# Реализовать на Python и отрисовать с помощью Matplotlib ряд из фигур
# Лисажу (4 графика) с разным соотношение частот (3:2), (3:4), (5:4), (5:6).

import numpy as np
import matplotlib.pyplot as plt


def lissajous_curve(a, b, delta, t):
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    return x, y

# Создаем массив значений времени от 0 до 2*pi с небольшим шагом
t = np.linspace(0, 2 * np.pi, 1000)

# Создаем 4 графика фигур Лисажу с разными соотношениями частот
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# 3:2
axs[0, 0].plot(*lissajous_curve(3, 2, 0, t))
axs[0, 0].set_title('3:2')

# 3:4
axs[0, 1].plot(*lissajous_curve(3, 4, 0, t))
axs[0, 1].set_title('3:4')

# 5:4
axs[1, 0].plot(*lissajous_curve(5, 4, 0, t))
axs[1, 0].set_title('5:4')

# 5:6
axs[1, 1].plot(*lissajous_curve(5, 6, 0, t))
axs[1, 1].set_title('5:6')


plt.suptitle('Ряд фигур Лисажу с разными соотношениями частот')

# Отображение графиков
plt.show()

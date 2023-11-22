# Реализовать с помощью Matplotlib анимацию врашения фигуры Лисажу
# при нулевом сдвиге фаз и изменении соотношения частот от 0 до 1

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def lissajous_curve(a, b, delta, t):
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    return x, y

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)


def init():
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    return line,


def update(frame):
    a = 3  # фиксированное значение для одной из частот
    b = frame  # изменение другой частоты от 0 до 1
    delta = 0  # нулевой сдвиг фаз
    t = np.linspace(0, 2 * np.pi, 1000)
    x, y = lissajous_curve(a, b, delta, t)
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, 100),
                    init_func=init, blit=True)

plt.title('Анимация вращения фигуры Лисажу')
plt.show()

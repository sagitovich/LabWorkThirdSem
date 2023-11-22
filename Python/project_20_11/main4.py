# Реализовать с помощью Matplotlib блок моделирования сложения 2 волн,
# включающий 2 интерактивных окна для задания исходных волн (как sin(x))
# минимальная интерактивность включат 2 слайдера регулирующих частоту и амплитуду волны.
# Кроме 2 интерактивных  окон должно присутствовать окно отображающее результат сложения 2х волн

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Создаем фигуру и оси для исходных волн
fig, (ax_wave1, ax_wave2, ax_result) = plt.subplots(3, 1, figsize=(8, 6))
plt.subplots_adjust(left=0.1, right=0.9, hspace=0.5)

# Начальные параметры волн
frequency1_init = 1.0
amplitude1_init = 1.0
frequency2_init = 2.0
amplitude2_init = 0.5

t = np.linspace(0, 2 * np.pi, 1000)

# Исходные волны
wave1, = ax_wave1.plot(t, amplitude1_init * np.sin(frequency1_init * t), lw=2, label='Волна 1')
wave2, = ax_wave2.plot(t, amplitude2_init * np.sin(frequency2_init * t), lw=2, label='Волна 2')

# Окно для результата сложения волн
result_wave, = ax_result.plot(t, np.zeros_like(t), lw=2, label='Результат')

# Настройка осей
ax_wave1.set_title('Волна 1')
ax_wave2.set_title('Волна 2')
ax_result.set_title('Результат сложения волн')

ax_wave1.legend()
ax_wave2.legend()
ax_result.legend()

# Создаем слайдеры
ax_freq1 = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_amp1 = plt.axes([0.1, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_freq2 = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_amp2 = plt.axes([0.1, 0.2, 0.65, 0.03], facecolor='lightgoldenrodyellow')

s_freq1 = Slider(ax_freq1, 'Частота 1', 0.1, 10.0, valinit=frequency1_init)
s_amp1 = Slider(ax_amp1, 'Амплитуда 1', 0.1, 2.0, valinit=amplitude1_init)
s_freq2 = Slider(ax_freq2, 'Частота 2', 0.1, 10.0, valinit=frequency2_init)
s_amp2 = Slider(ax_amp2, 'Амплитуда 2', 0.1, 2.0, valinit=amplitude2_init)


def update(val):
    freq1 = s_freq1.val
    amp1 = s_amp1.val
    freq2 = s_freq2.val
    amp2 = s_amp2.val

    wave1.set_ydata(amp1 * np.sin(freq1 * t))
    wave2.set_ydata(amp2 * np.sin(freq2 * t))

    result_wave.set_ydata(amp1 * np.sin(freq1 * t) + amp2 * np.sin(freq2 * t))

    fig.canvas.draw_idle()

s_freq1.on_changed(update)
s_amp1.on_changed(update)
s_freq2.on_changed(update)
s_amp2.on_changed(update)

plt.show()

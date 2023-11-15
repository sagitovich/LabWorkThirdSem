# Написать программу NumPy генерирующую массив случайных чисел нормального распределения размера 10х4. 
# Найти минимальноe, максимальное, средние значения, стандартное отклонение. Сохранить первые 5 строк в отдельную переменную.

import numpy as np

row = 10
column = 4

normal_random_array = np.random.randn(row, column)
print(f'\n{normal_random_array}\n')

minValue = np.min(normal_random_array)
print(f'Min value: {minValue}\n')

maxValue = np.max(normal_random_array)
print(f'Max value: {maxValue}\n')

meanValue = np.mean(normal_random_array)
print(f'Mean value: {meanValue}\n')

stdDevValue = np.std(normal_random_array)
print(f'Standart deviation value: {stdDevValue}\n')

selectRows = normal_random_array[0:5, :]
print(f'First five rows: \n{selectRows}\n')


# Найти максимальный элемент в векторе x среди элементов, перед которыми стоит нулевой. 
# Для x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0]) ответ 5.

import numpy as np 

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
maxValue = -(10**10)

i = 0
while i < len(x):
    while (i < len(x) - 1) and (x[i] == 0) and (x[i+1] > maxValue):
        maxValue = x[i+1]
    i += 1

print(f'Vector: {x}')
print(f'Max value: {maxValue}')




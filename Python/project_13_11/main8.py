# Найти индексы ненулевых элементов в [0,1,2,0,0,4,0,6,9]

import numpy as np 

vector = np.array([0,27,44,0,0,14,0,62,91]) 

indices = np.where(vector != 0)

print(f'\nИндексы ненулевых элементов: {indices}')
print(f'Элементы под индексами ненулевых элементов: {vector[indices]}\n')

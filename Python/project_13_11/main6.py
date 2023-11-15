# Поменять местами две строки в двумерном массиве NumPy -  поменяйте  строки 1 и 3 массива а. 
# a = np.arange(16).reshape(4,4)

import numpy as np 

a = np.arange(25).reshape(5, 5)
print(f'\nBase matrix: \n{a}\n')

a[[1, 3]] = a[[3, 1]]
print(f'New matrix: \n{a}\n')

# Найти уникальные значения и их количество в столбце species таблицы iris.

import numpy as np 

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

with_out = iris[:, :-1]
uni = np.unique(with_out)

print(f'\nУникальные значения: \n{uni}\n')
print(f'Количество уникальных значений: {len(uni)}\n')
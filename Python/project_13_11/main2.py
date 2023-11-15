# Реализовать кодирование длин серий (Run-length encoding). Дан вектор x. 
# Необходимо вернуть кортеж из двух векторов одинаковой длины. 
# Первый содержит числа, а второй - сколько раз их нужно повторить. 
# Пример: x = np.array([2, 2, 2, 3, 3, 3, 5]). Ответ: (np.array([2, 3, 5]), np.array([3, 3, 1])).

import numpy as np

x = np.array([3, 3, 2, 2, 2, 5])
element = np.array([], dtype=int)
count = np.array([], dtype=int)

i = 0
while i < len(x):
    tempCnt = 1
    element = np.append(element, x[i])
    while i < len(x)-1 and x[i] == x[i+1]:
        tempCnt += 1
        i += 1
    count = np.append(count, tempCnt)
    i += 1

print(f'Original vector: {x}')
print(f'Answer: {element}, {count}')

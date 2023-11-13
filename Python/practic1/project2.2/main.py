n = int(input('Введите количество рядов лесенки: '))
a = []
b = []

i = 1
k = 0
while i < n + 1:
    for j in range(i, n+1):
        a.append(j)
        b = a[:-1]

        print(' '*(n-1-k), *a, *b[::-1], ' '*(n-2-k), sep='')

        k += 1
        i += 1

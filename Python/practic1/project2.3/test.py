n = int(input('Введите количество рядов лесенки: '))
a = []
b = []

k = 0
q = 11
i = 1

while i < n + 1:
    for j in range(i, n+1):
        a.append(j)

        if len(str(a[-1])) == 1:
            temp1 = ' ' * (n * len(str(n)) - 1 - k)
            print(temp1, *a[::-1], *a[1:], sep='')
            k += 1

        if len(str(a[-1])) == 2:     # нужно заменить двойку на чо-то умное
            temp2 = ' ' * (n * len(str(n)) - q)
            print(temp2, *a[::-1], *a[1:], '\n', sep='')
            q += len(str(n))

        i += 1
        # k += 1


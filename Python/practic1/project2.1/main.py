# n = int(input('Введите количество рядов лесенки: '))
# a = []
#
# i = 1
# while i < n + 1:
#     for j in range(i, n+1):
#         a.append(j)
#         print(*a)
#         i += 1


n = int(input('Введите количество рядов лесенки: '))
num = ''

for i in range(1, n+1):
    num += str(i)
    print(num)


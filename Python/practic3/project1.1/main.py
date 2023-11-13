str = input('Введите строку: ')

if not str.isascii():
    print('Строка некорректна')
    exit()

temp = []
i, cnt = 0, 0
k = i + 1
while k < len(str) - 1:

    if str[k].isdigit():
        cnt = int(str[k])       # какая цифра стоит после буквы
        for j in range(cnt):    # столько раз добавим в список
            temp.append(str[i]) # эту букву
        i = k + 1
        k = i + 1
    else:
        temp.append(str[i])
        i = k 
        k = i + 1

if str[-1].isdigit():
    for j in range(int(str[-1])):    # столько раз добавим в список
            temp.append(str[-2])
else:
    temp.append(str[-2])
    temp.append(str[-1])

print(*temp, sep='')

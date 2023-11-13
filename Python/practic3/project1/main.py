str = input('Введите строку: ')

if not (str.isascii() and str.isalpha()):
    print('Строка некорректна')
    exit()

temp = []
i, k, cnt = 0, 1, 1
# i - символ, с которым сравниваем
# k - символ, который сравниваем
# cnt - количество повторений символа

temp.append(str[i])
while k != len(str):

    if str[i] == str[k]:
        cnt += 1
        k += 1
    else:
        if cnt != 1:
            temp.append(cnt)
        i = k 
        temp.append(str[i])
        k += 1
        cnt = 1
if cnt != 1:
    temp.append(cnt)

print(*temp, sep='')

str = input('Введите строку: ')
str = str.split(' ')
temp = ''
for i in range(len(str)):
    temp += str[i]

maxCount = 0
maxLetter = ''
for i in range(len(temp)):
    cnt = 0
    cnt = temp.count(temp[i])
    if cnt > maxCount:
        maxCount = cnt 
        maxLetter = temp[i]

print(f'Количество букв "{maxLetter}" в исходной строке максимально и равно {maxCount}.')
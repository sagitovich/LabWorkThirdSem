# task: Сохранить этот текст в файл. Прочитать матрицу из файла.
#   Hайдите для этой матрицы сумму всех элементов, максимальный и минимальный элемент (число)
#    3,4,17,-3
#    5,11,-1,6
#    0,2,-5,8


matrix = [] # создали матрицу 

with open("output_matrix.txt") as file: 
    for line in file:
        row = [] 
        # разделяем каждую строку по запятым
        for element in line.strip().split(','):
            row.append(int(element))
        # добавляем строку в матрицу
        matrix.append(row)

row = len(matrix)           # строки матрицы
column = len(matrix[0])     # столбцы матрицы

print('\n', 'Matrix:')
for i in range(row):
    print(*matrix[i])

sumOfElements = 0
for i in range(row):
    for j in range(column):
        sumOfElements += matrix[i][j]
print(f'\nSum of elements of matrix: {sumOfElements}')

maxElement = -(10**100)
minElement = 10**100
for i in range(row):
    for j in range(column):
        if matrix[i][j] > maxElement:
            maxElement = matrix[i][j]
        elif matrix[i][j] < minElement:
            minElement = matrix[i][j]
print(f'Max element of matrix: {maxElement}')
print(f'Min element of matrix: {minElement}')


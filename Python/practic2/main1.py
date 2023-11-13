n = int(input('Введите число строк треугольнка Паскаля: '))

def Triangle(rows):
    k = 0
    i = 1
    row = [1]
    for _ in range(rows):

        print(' '*(n-1-k), *row, '\n', sep=' ')
        row = [sum(x) for x in zip([0]+row, row+[0])]
        k += 1

Triangle(n)


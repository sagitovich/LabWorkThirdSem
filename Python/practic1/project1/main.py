def func(a, b, c):
    if a == b == c:
        return 3

    elif (a == b and a != c) \
            or (a != b and b == c) \
            or (a == c and b != c):
        return 2

    else:
        return 0

n1, n2, n3 = map(float, input('Введите три числа через пробел: ').split(' '))
print(func(n1, n2, n3))

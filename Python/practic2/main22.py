def printSierpinski(n) :
    y = n - 1
    while(y >= 0) :
        # заполняем пространство
        # до значения Y
        i = 0
        while(i < y ):
            print(" ", end="")
            i += 1
        x = 0
        while(x + y < n):
            if ((x & y) != 0) :
                print(" ", end = " ")
            else :
                print("* ", end = "")
            x = x + 1
        print()
        y -= 1


n = int(input('Введите размер основания треугольника Серпинского: '))
printSierpinski(n)

class Vector:
    def __init__(self, *args):
        if len(args) == 0:
            # Если не переданы аргументы, устанавливаем координаты вектора в нули по умолчанию.
            self.x = self.y = self.z = 0
        elif len(args) == 1:
            if isinstance(args[0], (list, tuple)):
                if len(args[0]) == 3:
                    # Если передан список или кортеж из трех чисел, используем их как координаты.
                    self.x, self.y, self.z = args[0]
                else:
                    raise ValueError("Список или кортеж должен содержать три числа.")
            elif isinstance(args[0], int):
                # Если передано одно целое число, устанавливаем все координаты вектора равными этому числу.
                self.x = self.y = self.z = args[0]
            else:
                raise ValueError("Недопустимый тип аргумента.")
        elif len(args) == 3:
            # Если переданы три аргумента, используем их как координаты.
            self.x, self.y, self.z = args
        else:
            raise ValueError("Недопустимое количество аргументов. Передайте 0, 1 или 3 аргумента.")


    def __abs__(self):
        return self.length()


    def length(self):
        # Вычисляем длину вектора.
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


    def __add__(self, other):
        if isinstance(other, Vector):
            # Перегружаем оператор сложения для векторов.
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise ValueError("Вектор можно складывать только с другим вектором.")


    def __sub__(self, other):
        if isinstance(other, Vector):
            # Перегружаем оператор вычитания для векторов.
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise ValueError("Из вектора можно вычитать только другой вектор.")


    def __neg__(self):
        # Перегружаем унарный минус, который равносилен умножению вектора на -1.
        return Vector(-self.x, -self.y, -self.z)


    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            # Перегружаем оператор умножения вектора на число.
            return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
        else:
            raise ValueError("Вектор можно умножать только на скаляр (целое число или число с плавающей запятой).")


    def dot_product(self, other):
        if isinstance(other, Vector):
            # Вычисляем скалярное произведение двух векторов.
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise ValueError("Скалярное произведение определено только для двух векторов.")


    def cross_product(self, other):
        if isinstance(other, Vector):
            # Вычисляем векторное произведение двух векторов.
            return Vector(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x,
            )
        else:
            raise ValueError("Векторное произведение определено только для двух векторов.")


    @staticmethod
    def triple_product(a, b, c):
        # Вычисляем смешанное произведение векторов a, b и c.
        return a.dot_product(b.cross_product(c))


    def __or__(self, other):
        if isinstance(other, Vector):
            # Перегружаем оператор | (pipe) для проверки коллинеарности векторов.
            return self.cross_product(other) == Vector(0, 0, 0)


    @staticmethod
    def are_complanar(a, b, c):
        # Проверяем компланарность векторов a, b и c.
        return a.triple_product(a, b, c) == 0


    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


# Создаем векторы
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 19)
print()
print("Координаты v1:", v1.__str__())
print("Координаты v2:", v2.__str__())
print("Координаты v3:", v3.__str__())
print()

# Метод length - вычисление длины вектора
print("Длина v1:", v1.length())
print("Длина v2:", v2.length())
print("Длина v3:", v3.length())
print()

# Метод abs - перегрузка стандартной функции abs
print("Абсолютное значение v1:", abs(v1))
print("Абсолютное значение v2:", abs(v2))
print("Абсолютное значение v3:", abs(v3))
print()

# Оператор сложения векторов (+)
v_sum = v1 + v2
print("Сумма v1 и v2:", v_sum)
print()

# Оператор вычитания векторов (-)
v_diff = v1 - v2
print("Разность v1 и v2:", v_diff)
print()

# Унарный минус (-)
v_neg = -v1
print("Унарный минус v1:", v_neg)
print()

# Оператор умножения вектора на скаляр (*)
v_scaled1 = v1 * 2
v_scaled2 = v2 * 5
v_scaled3 = v3 * 9
print("Умножение v1 на скаляр 2:", v_scaled1)
print("Умножение v2 на скаляр 5:", v_scaled2)
print("Умножение v3 на скаляр 9:", v_scaled3)
print()

# Скалярное произведение векторов (dot_product)
dot_product_result = v1.dot_product(v2)
print("Скалярное произведение v1 и v2:", dot_product_result)
print()

# Векторное произведение векторов (cross_product)
cross_product_result = v1.cross_product(v2)
print("Векторное произведение v1 и v2:", cross_product_result)
print()

# Смешанное произведение векторов (triple_product)
triple_product_result = Vector.triple_product(v1, v2, v3)
print("Смешанное произведение v1, v2 и v3:", triple_product_result)
print()

# Проверка коллинеарности векторов (|)
are_collinear = v1 | v3
print("v1 и v3 коллинеарны:", are_collinear)
print()

# Проверка компланарности векторов (are_complanar)
are_complanar = Vector.are_complanar(v1, v2, v3)
print("v1, v2 и v3 компланарны:", are_complanar)
print()

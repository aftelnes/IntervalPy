#Меньшая граница до ближайшего машинного числа с недостатком, а большая для блажайшего машинного с избытком

#КАЛЬКУЛЯТОР В ЛАБАХ НА БАЗАХ БУСТА
#Элементарные функции - sin, cos.., Разложение в Тейлора
#Задачи линала, умножение матриц, слау, определитель, обратная

#ПРИСТАТЬ К АНЕ НА СЧЁТ ПРОВЕРКИ
import math

class Interval:

    _x1: float = 0.0
    _x2: float = 1.0

    def __init__(self, x1 = 1, x2 = None):
        if x2 == None:
            self._x1 = x1
            self._x2 = x1
        elif x1 >= x2:
            self._x1 = x2
            self._x2 = x1
        else:
            self._x1 = x1
            self._x2 = x2

    #Переопределение алгебраических операций Begin
    def __add__(self, other):
        """Переопределение операторы сложения для интервала"""
        if (type(other) == int or type(other) == float):
            x1 = self._x1 + other
            x2 = self._x2 + other
        else:
            x1 = self._x1 + other._x1
            x2 = self._x2 + other._x2
        return Interval(x1, x2)

    def __sub__(self, other):
        """Переопределение операторы вычитания для интервала"""
        if (type(other) == int or type(other) == float):
            x1 = self._x1 - other
            x2 = self._x2 - other
        else:
            x1 = self._x1 - other._x2
            x2 = self._x2 - other._x1
        return Interval(x1, x2)

    def __mul__(self, other):
        """Переопределение умножения вычитания для интервала"""
        if (type(other) == int or type(other) == float):
            x1 = self._x1 * other
            x2 = self._x2 * other
        else:
            x1 = min(self._x1*other._x2, self._x2*other._x1)
            x2 = max(self._x1*other._x1, self._x2*other._x2)
        return Interval(x1, x2)

    def __truediv__(self, other):
        """Переопределение деления для интервала"""
        if (type(other) == int or type(other) == float):
            x1 = self._x1 / other
            x2 = self._x2 / other
        else:
            interval2_x1 = (1/other._x2)
            interval2_x2 = (1/other._x1)
            interval2 = Interval(interval2_x1, interval2_x2)
            return self*interval2
        return Interval(x1, x2)

    def __pow__(self, power):
        """Переопределение возведения в степень для интервала"""
        if (0 < self._x1 or power % 2 != 0):
            x1 = pow(self._x1, power)
            x2 = pow(self._x2, power)
        elif (self._x1 <= 0 and self._x2 >= 0 and power % 2 == 0):
            x1 = 0.0
            x2 = pow(abs(self._x2), power)
        elif (self._x2 < 0 and power % 2 == 0):
            x1 = pow(self._x2, power)
            x2 = pow(self._x1, power)
        return Interval(x1, x2)

    def __eq__(self, other) -> bool:
        """Переопределение равенства для интервала"""
        if (self._x1 == other._x1 and self._x2 == other._x2):
            return True
        else:
            return False

    # Переопределение алгебраических операций End


    #Функционал Begin
    @classmethod
    def positive_sign(cls, interval_1):
        """Метод проверяет интервал на положительность"""
        if (interval_1._x1 > 0) and (interval_1._x2 > 0):
            return True
        else:
            return False

    @classmethod
    def negative_sign(cls, interval_1):
        """Метод проверяет интервал на отрицательность"""
        if (interval_1._x1 < 0) and (interval_1._x2 < 0):
            return True
        else:
            return False

    @classmethod
    def difference(cls, interval_1, interval_2):
        """Метод возвращает разность множеств"""
        if (interval_1._x2 >= interval_2._x1) and (interval_1._x1 < interval_2._x1):
            left_x1 = interval_1._x1
            left_x2 = interval_2._x1
            right_x1 = interval_1._x2
            right_x2 = interval_2._x2
            return (Interval(left_x1, left_x2), Interval(right_x1, right_x2))
        elif (interval_2._x2 >= interval_1._x1) and (interval_1._x1 > interval_2._x1):
            left_x1 = interval_2._x1
            left_x2 = interval_1._x1
            right_x1 = interval_2._x2
            right_x2 = interval_1._x2
            return (Interval(left_x1, left_x2), Interval(right_x1, right_x2))
        else:
            print('У этих интервалов нет пересечения => нет разности')

    @classmethod
    def intersection(cls, interval_1, interval_2):
        """Метод возвращает перессечение множеств"""
        if interval_1._x2 >= interval_2._x1:
            x1 = interval_1._x1
            x2 = interval_2._x2
            return Interval(x1, x2)
        elif interval_2._x2 <= interval_1._x1:
            x1 = interval_2._x1
            x2 = interval_1._x2
            return Interval(x1, x2)
        else:
            print('У этих интервалов нет пересечения')

    @classmethod
    def union(cls, interval_1, interval_2):
        """Метод возвращает объединение множеств"""
        if (interval_1._x2 >= interval_2._x1) and (interval_1._x1 < interval_2._x1):
            x1 = interval_1._x1
            x2 = interval_2._x2
            return Interval(x1, x2)
        elif (interval_2._x2 >= interval_1._x1) and (interval_1._x1 > interval_2._x1):
            x1 = interval_2._x1
            x2 = interval_1._x2
            return Interval(x1, x2)
        else:
            print('У этих интервалов нет объединения')

    @classmethod
    def sum(cls, interval_1, interval_2, precision: float = 0.001):
        """Метод сложения интервалов, позволяющий указать определённую точность"""
        x1 = interval_1._x1 + interval_2._x1
        x2 = interval_1._x2 + interval_2._x2
        return Interval(Interval.round_down_with_precision(x1, precision),
                        Interval.round_up_with_precision(x2, precision))

    @classmethod
    def sub(cls, interval_1, interval_2, precision: float = 0.001):
        """Метод вычитания интервалов, позволяющий указать определённую точность"""
        x1 = interval_1._x1 - interval_2._x2
        x2 = interval_1._x2 - interval_2._x1
        return Interval(Interval.round_down_with_precision(x1, precision),
                        Interval.round_up_with_precision(x2, precision))

    @classmethod
    def mul(cls, interval_1, interval_2, precision: float = 0.001):
        """Метод умножения интервалов, позволяющий указать определённую точность"""
        x1 = min(interval_1._x1 * interval_2._x2, interval_1._x2 * interval_2._x1)
        x2 = max(interval_1._x1 * interval_2._x1, interval_1._x2 * interval_2._x2)
        return Interval(Interval.round_down_with_precision(x1, precision),
                        Interval.round_up_with_precision(x2, precision))

    @classmethod
    def div(cls, interval_1, interval_2, precision: float = 0.001):
        """Метод деления интервалов, позволяющий указать определённую точность"""
        interval_2 = Interval(1 / interval_2._x2, 1 / interval_2._x1)
        x1 = min(interval_1._x1 * interval_2._x2, interval_1._x2 * interval_2._x1)
        x2 = max(interval_1._x1 * interval_2._x1, interval_1._x2 * interval_2._x2)

        return Interval(Interval.round_down_with_precision(x1, precision),
                        Interval.round_up_with_precision(x2, precision))

    @classmethod
    def power(cls, interval, degree):
        """Возведение в степень"""
        int_res = Interval(1, 1)
        for i in range(degree):
            int_res = int_res * interval

        return int_res

    def contain(self, interval_2) -> bool:
        """Проверяет вклчает ли один интервал другой"""
        if (self._x1 <= interval_2._x1 and self._x2 >= interval_2._x2):
            return True
        else:
            return False

    def wid(self) -> float:
        """Возвращает ширину интервала"""
        return self._x2 - self._x1

    def mid(self) -> float:
        """Возвращает середину интервала"""
        return (self._x2 + self._x1)/2

    def rad(self) -> float:
        """Возвращает радиус интервала"""
        return (self._x2 - self._x1)/2

    def abs_val(self) -> float:
        """Возвращает абсолютную величину"""
        return max(abs(self._x1), abs(self._x2))

    def magn(self) -> float:
        """Возвращает магнитуду"""
        if (self._x1 < 0 and self._x2 > 0):
            return 0
        else:
            return min(abs(self._x1), abs(self._x2))

    def dev(self) -> float:
        """Возвращает отклонение"""
        if (abs(self._x1) >= abs(self._x2)):
            return self._x1
        else:
            return self._x2

    #Функционал End

    #Функцонал Линейной Алгебры Begin

    @classmethod
    def create_vector(cls, *args):
        res_ary = []
        for i in range(len(args)):
            print(args[i].show_interval())
            res_ary.append(args[i])
        print(f'res_ary = {res_ary}')
        return res_ary

    @classmethod
    def show_vector(cls, inter_vector):
        print(len(inter_vector))
        for i in range(len(inter_vector)):
            print(inter_vector[i].show_interval())


    @classmethod
    def gauss(cls, matrix, free_column, n):
        """Функция реализующая метод Гаусса для интервалов"""
        # Прямой ход
        for i in range(n):
            if matrix[i][i] == Interval(0, 0): raise ValueError("Ошибкa деления на 0")

            # Приведение уравнений к треугольному виду
            for j in range(i + 1, n):
                factor = matrix[j][i] / matrix[i][i]
                free_column[j] = free_column[j] - factor * free_column[i]
                for k in range(i, n):
                    matrix[j][k] = matrix[j][k] - factor * matrix[i][k]

        # Обратный ход
        result = [0] * n
        for i in range(n - 1, -1, -1):
            if matrix[i][i] == Interval(0, 0):
                raise ValueError("Ошибкa деления на 0")

            result[i] = free_column[i] / matrix[i][i]
            for j in range(i - 1, -1, -1):
                free_column[j] = free_column[j] - matrix[j][i] * result[i]

        return result

    @classmethod
    def matrix_mult(cls, matrix1, matrix2):
        """Умножение матриц"""
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        cols2 = len(matrix2[0])

        result = [[Interval(0, 0) for _ in range(cols2)] for _ in range(rows1)]

        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]

        return result


    @classmethod
    def matrix_add(cls, matrix1, matrix2):
        """Сложение матриц"""
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])

        if rows1 != rows2 or cols1 != cols2:
            return "У матриц должна быть одна размерность!"

        result = [[Interval(0, 0) for _ in range(cols1)] for _ in range(rows1)]

        for i in range(rows1):
            for j in range(rows1):
                result[i][j] = matrix1[i][j] + matrix2[i][j]

        return result

    @classmethod
    def matrix_sub(cls, matrix1, matrix2):
        """Разность матриц"""
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])

        if rows1 != rows2 or cols1 != cols2:
            return "У матриц должна быть одна размерность!"

        result = [[Interval(0, 0) for _ in range(cols1)] for _ in range(rows1)]

        for i in range(rows1):
            for j in range(cols1):
                result[i][j] = matrix1[i][j] - matrix2[i][j]

        return result

    #Функцонал Линейной Алгебры End


    #Функционал элементарных функций Begin

    @classmethod
    def sin(cls, interval):

        sin_left = math.sin(interval._x1)
        sin_right = math.sin((interval._x1 + interval._x2) / 2)

        x1 = min(sin_left, sin_right)
        x2 = max(sin_left, sin_right)

        return Interval(x1, x2)

    #Функционал элементарных функций End

    #Функции демонстрации мнформации Begin
    def show_interval(self, round_number: int = 15):
        print(f'[{round(self._x1, round_number)}, {round(self._x2, round_number)}]')

    def show_left_border(self, round_number: int = 15):
        print(f'{round(self._x1, round_number)}')

    def show_right_border(self, round_number: int = 15):
        print(f'{round(self._x2, round_number)}')

    # Функции демонстрации мнформации End


    #Вспомогательные функции для вычислений Begin
    @classmethod
    def round_up_with_precision(self, number: float, precision: float = 0.001):
        """Округление до ближайшего машшинного числа(с избытком) с определённой точность"""
        return math.ceil(number / precision) * precision

    @classmethod
    def round_down_with_precision(self, number: float, precision: float = 0.001):
        """Округление до ближайшего машшинного числа(с недостатком) с определённой точность"""
        return math.floor(number / precision) * precision

    # Вспомогательные функции для вычислений End



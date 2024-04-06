#Меньшая граница до ближайшего машинного числа с недостатком, а большая для блажайшего машинного с избытком

#КАЛЬКУЛЯТОР В ЛАБАХ НА БАЗАХ БУСТА
#логические (>=)
#Элементарные функции - sin, cos..
#Задачи линала, умножение матриц, слау, определитель, обратная

#ПРИСТАТЬ К АНЕ НА СЧЁТ ПРОВЕРКИ
import math

class Interval:

    _x1: float = 0.0
    _x2: float = 1.0

    def __init__(self, x1: float = 0.0, x2: float = 1.0):
        self._x1 = x1
        self._x2 = x2

    #Переопределение алгебраических операций Begin
    def __add__(self, other):
        """Переопределение операторы сложения для интервала"""
        x1 = self._x1 + other._x1
        x2 = self._x2 + other._x2
        return Interval(x1, x2)

    def __sub__(self, other):
        """Переопределение операторы вычитания для интервала"""
        x1 = self._x1 - other._x1
        x2 = self._x2 - other._x2
        return Interval(x1, x2)

    def __mul__(self, other):
        """Переопределение умножения вычитания для интервала"""
        x1 = min(self._x1*other._x2, self._x2*other._x1)
        x2 = max(self._x1*other._x1, self._x2*other._x2)
        return Interval(x1, x2)

    def __truediv__(self, other):
        """Переопределение деления вычитания для интервала"""
        x1 = self._x1*(1/other._x2)
        x2 = self._x2*(1/other._x1)
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
        """Переопределение равенства в степень для интервала"""
        if (self._x1 == other._x1 and self._x2 == other._x2):
            return True
        else:
            return False

    # Переопределение алгебраических операций End

    #Переопределение логических операций Begin
    def __lt__(self, other):
        pass

    #Переопределение логических операций End


    #Функционал Begin
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
        x1 = interval_1._x1 - interval_2._x1
        x2 = interval_1._x2 - interval_2._x2
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
        x1 = interval_1._x1 * (1 / interval_2._x2)
        x2 = interval_1._x2 * (1 / interval_2._x1)
        return Interval(Interval.round_down_with_precision(x1, precision),
                        Interval.round_up_with_precision(x2, precision))

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

    # Функционал End

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

    # Вспомогательные функции для вычислений Begin



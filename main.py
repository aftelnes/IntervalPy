from Interval import Interval as I

# inter1 = I(12.11, 4.345)
# inter2 = I(2.654, 4.78)
inter1 = I(-1, 5)
inter2 = I(2, 3)
inter2_copy = I(2, 3)
inter5 = I(-4, -2)

#Проверка суммы
print('Суммы: ')
inter3 = inter2 + inter1
inter3.show_interval()

inter3 = I.sum(inter1, inter2, precision=0.0000000001)
inter3.show_interval()

#Проверка разности
print('Разности: ')
inter3 = inter1 - inter2
inter3.show_interval()

inter3 = I.sub(inter1, inter2, precision=0.00001)
inter3.show_interval()

#Проверка умножения
print('Умножения: ')
inter3 = inter1 * inter2
inter3.show_interval()

inter3 = I.mul(inter1, inter2, precision=0.00001)
inter3.show_interval()

#Проверка деления
print('Деления: ')
inter3 = inter1 / inter2
inter3.show_interval()

inter3 = I.div(inter1, inter2, precision=0.01)
inter3.show_interval()

#Проверка возведения в степень
print('Степень: ')
# inter3 = I.power(inter1, 2)
inter3 = pow(inter1, 2)
inter3.show_interval()

#Проверка других методов
print("Содержание равенства интервалов", inter2 == inter3)
print("Содержание одного интервала в другом", inter1.contain(inter2))
inter4 = I(-3, 1)
print('wid: ', inter4.wid())
print('mid: ', inter4.mid())
print('rad: ', inter4.rad())
print('abs_val: ', inter4.abs_val())
print('magn: ', inter4.magn())
print('dev: ', inter4.dev())




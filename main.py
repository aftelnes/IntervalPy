from Interval import Interval as I

inter1 = I(-1, 5)
inter2 = I(2, 3)
inter2_copy = I(2, 3)
inter5 = I(-4, -2)

#Проверка суммы
print('Сумма: ')
inter3 = inter2 + inter1
inter3.show_interval()
print("Сумма с точностью: ")
inter3 = I.sum(inter1, inter2, precision=0.0000000001)
inter3.show_interval()
print()

#Проверка разности
print('Разность: ')
inter3 = inter1 - inter2
inter3.show_interval()
print("Разность с точностью: ")
inter3 = I.sub(inter1, inter2, precision=0.00001)
inter3.show_interval()
print()


#Проверка умножения
print('Умножение: ')
inter3 = inter1 * inter2
inter3.show_interval()
print('Умножение с точностью: ')
inter3 = I.mul(inter1, inter2, precision=0.00001)
inter3.show_interval()
print()


#Проверка деления
print('Деление: ')
inter3 = inter1 / inter2
inter3.show_interval()
print('Деление с точностью: ')
inter3 = I.div(inter1, inter2, precision=0.01)
inter3.show_interval()
print()


#Проверка возведения в степень
print('Степень: ')
inter3 = pow(inter1, 2)
inter3.show_interval()
print()


#Проверка других методов
print("Содержание равенства интервалов", inter2 == inter3)
print("Содержание одного интервала в другом", inter1.contain(inter2))
inter4 = I(-3, 1)
print()

print('Интервальные методы: ')
print('wid: ', inter4.wid())
print('mid: ', inter4.mid())
print('rad: ', inter4.rad())
print('abs_val: ', inter4.abs_val())
print('magn: ', inter4.magn())
print('dev: ', inter4.dev())
print()

print('Объединение: ')
interUnion1 = I(2, 10)
interUnion2 = I(5, 12)
interUnion = I.union(interUnion2, interUnion1)
interUnion.show_interval()
print()

print('Пересечение: ')
interIntersect = I.intersection(interUnion2, interUnion1)
interIntersect.show_interval()
print()

print('разность: ')
interLeft, interRight = I.difference(interUnion2, interUnion1)
interLeft.show_interval()
interRight.show_interval()
print()

print('Положительность, отрицательность: ')
interPos = I(1, 10)
interNeg = I(-4, -1)
print(I.negative_sign(interPos))
print(I.positive_sign(interPos))
print(I.negative_sign(interNeg))
print(I.positive_sign(interNeg))
print()


print('Операции с вещественными и натуральными числами: ')
inter_test = I(5)
inter_test.show_interval()
inter_test2 = I(2, 6)
inter_test_res = inter_test + inter_test2
inter_test_res.show_interval()
print()
inter_test = I(-2.34)
inter_test.show_interval()
inter_test2 = I(-1, 2.345)
inter_test_res = inter_test + inter_test2
inter_test_res.show_interval()
print()



print('Операции с векторами: ')
print('Сложение: ')
vec1 = [I(1, 2), I(-3, 2), I(5)]
vec2 = [I(3, 5), I(-10), I(7, 12)]
vec_res = []*3
for i in range(3):
    vec_res.append(vec1[i] + vec2[i])
for i in range(len(vec_res)):
    vec_res[i].show_interval()
print('Вычитание: ')
vec1 = [I(1, 2), I(-3, 2), I(5)]
vec2 = [I(3, 5), I(-10), I(7, 12)]
vec_res = []*3
for i in range(3):
    vec_res.append(vec1[i] - vec2[i])
for i in range(len(vec_res)):
    vec_res[i].show_interval()
print()


print("Операции с матрицами: ")
print('Умножение: ')
matrix1 = [[I(-2, 1), I(-1, 2), I(0, 3), I(1, 4), I(2, 5)], [I(-3, 0), I(-2, 1), I(-1, 2), I(0, 3), I(1, 4)],
           [I(-4, -1), I(-3, 0), I(-2, 1), I(-1, 2), I(0, 3)], [I(-5, -2), I(-4, -1), I(-3, 0), I(-2, 1), I(-1, 2)],
           [I(-6, -3), I(-5, -2), I(-4, -1), I(-3, 0), I(-2, 1)]]
matrix2 = [[I(1, 4), I(2, 5), I(3, 6), I(4, 7), I(5, 8)], [I(0, 3), I(1, 4), I(2, 5), I(3, 6), I(4, 7)],
           [I(-1, 2), I(0, 3), I(1, 4), I(2, 5), I(3, 6)], [I(-2, 1), I(-1, 2), I(0, 3), I(1, 4), I(2, 5)],
            [I(-3, 0), I(-2, 1), I(-1, 2), I(0, 3), I(1, 4)]]

res = I.matrix_mult(matrix1, matrix2)
for i in range(len(res)):
    for j in range(len(res)):
        res[i][j].show_interval()


print()
print('Сложение: ')
res = I.matrix_add(matrix1, matrix2)
for i in range(len(res)):
    for j in range(len(res)):
        res[i][j].show_interval()

print()
print('Разность: ')
res = I.matrix_sub(matrix1, matrix2)
for i in range(len(res)):
    for j in range(len(res)):
        res[i][j].show_interval()
print()

print('Метод Гаусса: ')
matrix1 = [[I(2,3), I(-1, 1)], [I(-1, 2), I(2, 3)]]
free_coef = [I(-2, 2), I(-2, 1)]
gaus_res = I.gauss(matrix1, free_coef, 2)
for i in range(len(gaus_res)):
    gaus_res[i].show_interval()

print('Элементарные функции: ')
print('Pow: ')
inter = I(-1, 2)
ires = I.power(inter, 3)
ires.show_interval()
res2 = inter*inter*inter
res2.show_interval()
print()

print('Sin: ')
inter_for_sin = I(-3, 2)
res = I.sin(inter_for_sin)
res.show_interval()
print()
print('Cos: ')
inter_for_cos = I(-3, 2)
res = I.cos(inter_for_cos)
res.show_interval()
print()
print('exp: ')
I.exp(I(-3, 2)).show_interval()
print()
print('indicative: ')
I.indicative(2, I(4, 4.2)).show_interval()

print("Tan: ")
inter3 = I(-3, 3)
I.tan(inter3).show_interval()

print("Операции с матрицами: ")
print('Умножение: ')
matrix1 = [[I(3.16514, 4.30493), I(4.12031, 9.84751), I(0.870962, 1.43171), I(2.27003, 9.27655), I(1.49018, 3.27633)],
           [I(2.48644, 4.89407), I(0.300193, 3.37987), I(0.326241, 1.11968), I(3.20657, 4.67947), I(4.75873, 6.1484)],
           [I(4.14816, 6.14464), I(0.544925, 3.23541), I(0.513681, 7.31363), I(0.266167, 8.69829), I(2.06268, 6.15244)],
           [I(3.20083, 4.35041), I(0.773538, 9.46056), I(3.9372, 4.96617), I(4.17574, 5.04621), I(3.49991, 5.56024)],
           [I(1.1853, 165676), I(0.574415, 2.45872), I(4.57426, 8.942321), I(1.33887, 4.99568), I(1.55559, 3.74883)]]


matrix2 = [[I(2.89423, 4.3556), I(2.47654, 7.28885), I(2.09921, 6.88413), I(0.885017, 2.71574), I(0.991362, 4.81623)],
           [I(3.8149, 3.83158), I(0.212509, 9.45654), I(0.086542, 6.24432), I(0.351645, 9.84651), I(0.122083, 4.31436)],
           [I(1.3997, 1.46762), I(2.50441, 7.08174), I(2.73262, 8.2874), I(1.53181, 4.6283), I(2.11295, 8.81563)],
           [I(3.09488, 3.85893), I(2.11292, 4.98892), I(1.48034, 6.98908), I(0.00628575, 4.86753), I(4.19766, 7.80104)],
           [I(3.23803, 6.06496), I(2.49699, 4.43826), I(4.16533, 4.83801), I(1.0229, 5.4479), I(1.14617, 2.71861)]]

res = I.matrix_mult(matrix1, matrix2)
for i in range(len(res)):
    for j in range(len(res)):
        res[i][j].show_interval()

A = [[I(1, 1), I(1, 1)], [I(0, 0), I(1, 1)]]
B = [[I(1, 1), I(0, 0)], [I(-1, -1), I(1, 1)]]
C = [[I(-1, 1), I(0, 0)], [I(0, 0), I(-1, 1)]]
res = I.matrix_mult(A, I.matrix_mult(B, C))
for i in range(len(res)):
    for j in range(len(res)):
        res[i][j].show_interval()




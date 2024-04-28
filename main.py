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

print()
print()
print()
inter1 = I(2, 3)
inter2 = I(4, 9)
inter_vec = I.create_vector(inter1, inter2, inter4)
I.show_vector(inter_vec)


print()
print()
interUnion1 = I(2, 10)
interUnion2 = I(5, 12)
print('Объединение: ')
interUnion = I.union(interUnion2, interUnion1)
interUnion.show_interval()
print('Пересечение: ')
interIntersect = I.intersection(interUnion2, interUnion1)
interIntersect.show_interval()
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
print('Операции с вещ числами: ')
inter_test = I(5)
inter_test.show_interval()
inter_test2 = I(2, 6)
inter_test_res = inter_test + inter_test2
inter_test_res.show_interval()
inter_test_res = I.contain(inter_test2, inter_test)


print()
print('Операции с векторами: ')
vec1 = [I(1, 2), I(-3, 2), I(5)]
vec2 = [I(3, 5), I(-10), I(7, 12)]
vec_res = []*3
for i in range(3):
    vec_res.append(vec1[i] + vec2[i])
for i in range(len(vec_res)):
    vec_res[i].show_interval()


print()
print("Операции с матрицами: ")
print('Умножение: ')
# matrix1 = [[I(1,3), I(1)], [I(3), I(1, 3)]]
# matrix2 = [[I(1), I(-2, 0)], [I(0,2), I(1)]]

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
print()
print('Гаусс: ')
matrix1 = [[I(2,3), I(-1, 1)], [I(-1, 2), I(2, 3)]]
free_coef = [I(-2, 2), I(-2, 1)]
gaus_res = I.gauss(matrix1, free_coef)
for i in range(len(gaus_res)):
    gaus_res[i].show_interval()


print()
print()
print('Sin: ')
inter_for_sin = I(0, 1)
res = I.sin(inter_for_sin)
res = I.sin(inter_for_sin)
res.show_interval()

print()
print()
print('pow: ')
inter = I(-1, 2)
ires = I.power(inter, 3)
ires.show_interval()
res2 = inter*inter*inter
res2.show_interval()

inter1 = I(2, 3)
tmp = inter1 * (-1)
tmp.show_interval()
res = I(2, 3) / I(-3, -2)
res.show_interval()

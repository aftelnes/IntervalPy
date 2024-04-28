from Interval import Interval as I
def ia_Gauss(matrica_a, massiv_b, n):
    a = [[None for _ in range(n)] for _ in range(n)]
    b = [None] * n
    x = [None] * n

    for i in range(n):
        for j in range(n):
            a[i][j] = matrica_a[i][j]

        b[i] = massiv_b[i]

    for j in range(n - 1):
        for i in range(j + 1, n):
            rij = a[i][j] / a[j][j]

            for k in range(j + 1, n):
                a[i][k] = a[i][k] - rij * a[j][k]

            b[i] = b[i] - rij * b[j]

    for i in range(n - 1, -1, -1):
        summ = I(0, 0)

        for j in range(i+1, n):
            summ = summ + a[i][j] * I(j, j)

        x[i] = (b[i] - summ) / a[i][i]

    return x


# Пример с матрицами 3x3
# matrix1 = [[I(2,3), I(1, 1)], [I(-1, 2), I(2, 3)]]
# free_coef = [I(-2, 2), I(-2, 1)]

matrix1 = [[I(3.33,3.33), I(0, 2), I(0, 2)], [I(0, 2), I(3.33, 3.33), I(0, 2)], [I(0, 2), I(0, 2), I(3.33, 3.33)]]
free_coef = [I(-1, 2), I(-1, 2), I(-1, 2)]

x = ia_Gauss(matrix1, free_coef, 3)
for i in range(len(x)):
    x[i].show_interval()

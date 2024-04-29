from Interval import Interval as I

matrix1 = [[I(2,3), I(-1, 1)], [I(-1, 2), I(2, 3)]]
free_coef = [I(-2, 2), I(-2, 1)]

matr = [[1, 4, 6], [-3, 5, 7], [9, 4, 4]]
b = [1, 5, -2]



def solve_gauss(A, b):
    n = len(A)

    # Прямой ход
    for i in range(n):
        if A[i][i] == I(0, 0): raise ValueError("Ошибкa деления на 0")

        # Приведение уравнений к треугольному виду
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            b[j] = b[j] - factor * b[i]
            for k in range(i, n):
                A[j][k] = A[j][k] - factor * A[i][k]

    # Обратный ход
    x = [0] * n
    for i in range(n - 1, -1, -1):
        if A[i][i] == I(0, 0):
            raise ValueError("Ошибкa деления на 0")

        x[i] = b[i] / A[i][i]
        for j in range(i - 1, -1, -1):
            b[j] = b[j] - A[j][i] * x[i]

    return x

def solve_gauss2(A, b):
    n = len(A)

    # Прямой ход
    for i in range(n):
        if A[i][i] == I(0, 0): raise ValueError("Ошибкa деления на 0")

        # Приведение уравнений к треугольному виду
        for j in range(i + 1, n):
            factor = A[i][j] / A[i][i]
            for k in range(j + 1, n):
                A[j][k] = A[i][k] - factor * A[j][k]
            b[i] = b[i] - factor*b[j]

    # Обратный ход
    x = [0] * n
    for i in range(n - 1, -1, -1):
        if A[i][i] == I(0, 0):
            raise ValueError("Ошибкa деления на 0")

    for i in range(n):
        summ = I(0, 0)
        for j in range(i, n):
            summ = summ + A[i][j] * x[j]
        x[i] = (b[i] - summ) / A[i][i]

    return x

def ia_Gauss(a, b, n):
    x = [0] * n

    r = [[I(0, 0) for _ in range(n)] for _ in range(n)]

    for j in range(n - 1):
        temp = I(-1, -1)
        for i in range(j, n):
            print(f'i = {i}, j = {j}')
            r[i][j] = a[i][j] / (a[j][j] * temp)
            print(f'a[i][j]: ')
            a[i][j].show_interval()
            print(f'a[j][j]: ')
            a[j][j].show_interval()
            print(f'a[j][j]*temp: ')
            (a[j][j] * temp).show_interval()
            print(f'r[i][j]: ')
            r[i][j].show_interval()



            for k in range(j + 1, n):
                print(f'r[i][j]: ')
                r[i][j].show_interval()
                a[i][k] = a[i][k] - r[i][j] * a[j][k]
                print(f'i = {i}, j = {j}, k = {k}')
                print(f'a[j][k]: ')
                a[j][k].show_interval()
                print(f'r[i][j]: ')
                (r[i][j] * a[j][k]).show_interval()
                print(f'a[i][k]: ')
                a[i][k].show_interval()

            b[i] = b[i] - r[i][j] * b[j]
            print(f'b[i]: ')
            b[i].show_interval()

    for i in range(n-1, -1, -1):
        summ = I(0, 0)
        for j in range(i, n):
            summ = summ + a[i][j] * x[j]
        x[i] = (b[i] - summ) / a[i][i]

    return x


res = solve_gauss(matrix1, free_coef)
for i in range(len(res)):
    res[i].show_interval()
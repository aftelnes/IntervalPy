from Interval import Interval as I

matrix1 = [[I(1,3), I(1, 5), I(-3, 2)], [I(3), I(1, 3), I(2, 9)], [I(4), I(4, 6), I(-2, 4)]]
free_coef = [I(2, 6), I(-3), I(-4, 6)]

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

res = solve_gauss(matrix1, free_coef)
for i in range(len(res)):
    res[i].show_interval()
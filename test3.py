import math

from Interval import Interval as I


inter = I(-10, 10)
k = 3

def Teylor_sin(inter, k):
    res_left = 0
    res_left += ((-1)**k)*((pow(inter._x1, 2*k+1))/(math.factorial(2*k+1)))
    res_right = 0
    res_right += ((-1) ** k) * ((pow(inter._x2, 2 * k + 1)) / (math.factorial(2 * k + 1)))
    print(res_left)
    print(res_right)

Teylor_sin(inter, k)
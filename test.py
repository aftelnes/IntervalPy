from Interval import Interval as I


#Тестируем переопределения оператора сложения, функция __add__
print('Тестируем переопределения оператора сложения, функция __add__ : ')
inter1 = I(-1, 4)
inter2 = I(2, 5)
result = inter1 + inter2
print('[-1, 4] + [2, 5] : ')
result.show_interval()
print(' ')
inter1 = I(-100, 25.324)
inter2 = I(0.00345, 123)
result = inter1 + inter2
print('[-100, 25.324] + [0.00345, 123] : ')
result.show_interval()

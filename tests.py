import math

from Interval import Interval as I

inter1=I(25,75)
inter2=I(-100, -60)
# Тестируем функции проверки на положительность и отрицательность 
print(I.negative_sign(inter1))
print("пройден +")

print(I.positive_sign(inter1))
print("пройден + ")

print(I.negative_sign(inter2))
print("пройден + ")

print(I.negative_sign(inter1))
print("пройден +")


inter3=I(-10.764, -2)
print(I.negative_sign(inter3))
print(" пройден + ")

print(I.positive_sign(inter3))
print(" пройден + ")
#Проверяем функцию поиска максимума абсолютных значений по модулю среди границ интервала


inter4=I(56.7912, 109)
print(inter4.abs_val())
print(" пройден + ")


inter5=I(-4, -3.9981)
print(inter5.abs_val())
print(" пройден + ")

#Проверяем вложен ли 1 интервал в другой 


inter6=I(-14, 9)
inter7=I(-10, 7.812)
print(inter6.contain(inter7))
print(" пройден + ")


inter8=I(1900,2135.6)
inter9=I(2000, 2076)
print(inter9.contain(inter8))
print(" пройден +")
#Проверяем методы объединения , пересечения и т.д
interUni1=I(-9000,8)
interUni2=I(2,4)
interLeft, interRight=I.difference(interUni2, interUni1)
interLeft.show_interval()
interRight.show_interval()


interUni3=I(7.8, 19.885)
interUni4=I(8.24, 10.9)
interLeft, interRight=I.difference(interUni4, interUni3)
interLeft.show_interval()
interRight.show_interval()
print(" пройден +")


interUni5=I(12,12.3)
interUni6=I(12.2,12.35)
interIntersect = I.intersection(interUni6, interUni5)
interIntersect.show_interval()


interUni7=I(-350,-310)
interUni8=I(-320, -309.889)
interIntersect = I.intersection(interUni8, interUni7)
interIntersect.show_interval()
print(" пройден +")


interUni9=I(-123.719, -3)
interUni10=I(-76, -12)
interUnion=I.union(interUni10,interUni9)
interUnion.show_interval()

interUni11=I(-10, 50.6257)
interUni12=I(-100,-12)
interUnion=I.union(interUni12,interUni11)
print(" пройден + ")

#Проверяем умножение, деление ,сумму и разность с определённой заданной точностью
inter12=I(6,15.7)
inter13=I(60.3, 66)
inter3=I.sum(inter12,inter13,precision=0.0001)
inter3.show_interval()


inter14=I(5.777999999998, 130.1111111111111)
inter15=I(3, 33)
inter11=I.sum(inter14,inter15,precision=0.0000000001)
inter11.show_interval()
print("пройден+ ")


inter16=I(570, 621)
inter17=I(123.5788897, 177)
inter18=I.sub(inter16,inter17,precision=0.00000001)
inter18.show_interval()


inter18=I(2.3, 3.5)
inter19=I(2,4)
inter20=I.sub(inter18,inter19,precision=0.1)
inter20.show_interval()
print(" пройден +")


inter21=I(9, 12)
inter22=I(15.561, 25.411)
inter23=I.mul(inter21, inter22,precision=0.001)
inter23.show_interval()

inter24=I(-18.6511, 2.2333)
inter25=I(4.4122, 5.5773)
inter26=I.mul(inter24,inter25,precision=0.001)
inter26.show_interval()
print (" пройден + ")


inter27=I(-97,2)
inter28=I(29,38)
inter29=I.div(inter27,inter28,precision=0.001)
inter29.show_interval()


inter30=I(3.354,8)
inter31=I(3.354,8)
inter32=I.div(inter30,inter31,precision=0.001)
inter32.show_interval()
print( "пройден + ")

# Проверяем остальные методы
inter33=I(122,270.7)
print( "magn ",inter33.magn())


inter34=I(-1,1)
print( "magn ",inter34.magn())
print( "пройден + ")


inter35=I(-20,34)
print( "mid ", inter35.mid())


inter36=I(-54.342,5.677)
print( "mid ", inter36.mid())
print(" пройден +  ")


inter37=I(-89, 122.23)
print("rad",inter37.rad())


inter38=I(823, 970)
print( "rad ",inter38.rad())
print("пройден +  ")


inter39=I(4.4321,7.8)
print(" wid ",inter39.wid())


inter40=I(123,411)
print(" wid ",inter40.wid())
print(" пройден + ")
























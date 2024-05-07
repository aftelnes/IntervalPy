from Interval import Interval as I


#Тестируем переопределения оператора сложения, функция __add__
print('Тестируем переопределения оператора сложения, функция __add__ : ')
inter1 = I(-1, 4)
inter2 = I(2, 5)
result = inter1 + inter2
print('[-1, 4] + [2, 5] : ')
result.show_interval()
print('Пройден ')
inter1 = I(-100, 25.324)
inter2 = I(0.00345, 123)
result = inter1 + inter2
print('[-100, 25.324] + [0.00345, 123] : ')
result.show_interval()
print("  пройден ")
#Не буду придумывать от себя ничего, не хочу руинить тебе работу
inter1=I(-111, 111)
inter2=I(100.25,178)
result=inter1+inter2
print('[-111, 111] + [100.25, 178] : ')
result.show_interval()
print(" пройден ")
inter1=I(200.32, 402)
inter2=I(-2, 35)
result=inter1+inter2
print('[200.32, 402]+ [-2, 35]: ')
result.show_interval()
print(" пройден ")
inter1=I(2.3575, 8)
inter2=I(122, 2577210)
result=inter1+inter2
print('[2.3575,  8]+[122, 2577210]: ')
result.show_interval()
print( "пройден" )
#Тестируем переопределение оператора вычитания, функция __sub__
print(" Тестируем операцию вычитания ")
inter1=I(20, 80)
inter2=I(33.4, 83.75)
result=inter1-inter2
print('[20, 80]- [33.4, 83.75]: ')
result.show_interval()
print(" пройден ")
inter1=I(403.4, 550)
inter2=I(403.4, 550)
result=inter1-inter2
print('[403.4, 550]-[403.4, 550]: ')
result.show_interval()
print("пройден ")
inter1=I(100.7721, 324)
inter2=I(90, 276.5892)
result=inter1-inter2
print('[100.7721, 324]-[90, 276.5892]: ')
result.show_interval()
print(" не пройден")
inter1=I(88.741, 109)
inter2=I(2000, 21000)
result=inter1-inter2
print('[88.741, 109]-[2000, 21000]: ')
result.show_interval()
print("пройден ")
inter1=I(88.91, 3500)
inter2=I(65, 250)
result=inter1-inter2

print('[88.91, 3500]-[65, 250]; ')
result.show_interval()
print( " не пройден ")
#тестируем переопределение оператора деления вычитания, функция__truediv__
print(" Тестируем операцию деления ")
inter1=I(100, 102)
inter2=I(180, 1222)
result=inter1/inter2
print("[100, 102]/[180,1222]: ")

result.show_interval()
print("пройден ")
inter1=I(1.11, 1.93)
inter2=I(2.25, 9.91)
result=inter1/inter2
print("[1.11, 1.93]/[2.25, 9.91]: ")

result.show_interval()
print("не пройден ")
inter1=I(-20.2, 6.7)
inter2=I(-20.1, 6.7)
result=inter1/inter2
print("[-20.2, 6.7]/[-20.1,6.7]: ")
result.show_interval()
print("не пройден ")
inter1=I(207.712,407.123)
inter2=I(16.234, 90.218)
result=inter1/inter2
print("[207.712, 407.123]/[16.234, 90.218]: ")
result.show_interval()
print("не пройден ")
inter1=I(10.19022, 17.83411)
inter2=I(5.55555, 9.77777)
result=inter1/inter2
print('[10.19022, 1783411]/[5.55555, 9.77777]: ')
result.show_interval()
print(" не пройден")
# Проверяем умножение для интервалов
inter1=I(2, 2.25)
inter2=I(4, 4.75)
result=inter1*inter2
print("[2, 2.25]*[4, 4.75]:")
result.show_interval()
print("Пройден ")


inter1=I(19.38, 274.94)
inter2=I(-1,1)
result=inter1*inter2
print("[19.38, 274.94]*[-1,1]: ")
result.show_interval()
inter1=I(20.012, 38.977)
inter2=I(60.617, 78.231)
result=inter1*inter2
print("[20.012, 38.977]*[60.617, 78.231]: ")
result.show_interval()

inter1=I(40, 88)
inter2=I(140, 188)
result=inter1*inter2
print("[40, 88]*[140, 188]: ")
result.show_interval()
inter1=I(-10.378, 50.971)
inter2=I(51.543, 52.071)
result=inter1*inter2
print("[-10.378, 50.971]*[51.543, 52.071]: ")
result.show_interval()
#Проверяем сравнение интервалов
inter1=I(2,4.45)
inter2=I(3, 6)
result=inter1==inter2
print("[2,4.45]==[3,6]: ")
print(result)
print(" пройден ")
inter1=I(2,5)
inter2=I(2,5.1)
result=inter1==inter2
print("[2, 5]==[2, 5.1]: ")
print(result)
print("пройден ")
inter1=I(10, 15)
inter2=I(10, 15)
result=inter1==inter2
print("[10, 15]==[10, 15]: ")
print(result)
print( "пройден ")
inter1=I(20.221,40.738)
inter2=I(2,2.5)
result=inter1==inter2
print("[20.221,40.738]==[2,2.5]: ")
print(result)
print(" пройден ")
inter1=I(1999.35, 2021.44)
inter2=I(1999.35, 2021.44)
result=inter1==inter2
print(" [1999.35, 2021.44]==[1999.35, 2021.44]: ")
print (result)
print( "пройден ")












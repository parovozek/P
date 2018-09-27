import math as m
class My1(object):
    """Class"""
    def __init__(self, x1,y1,x2,y2,x3,y3):
        """Constructor"""
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def __del__(self):
        print("Мусор удален!")

class MyMath(My1):
    """Class"""
    def result_function(self):
        s = m.sqrt(self.x1**2 + self.y1**2 + self.x2**2 + self.y2**2 + self.x3**2 +self.y3**2)
        return round(s,2)


    

#Вектор №1
x1 = int(input("Введите X1: "))
y1 = int(input("Введите Y1: "))
x2 = int(input("Введите X2: "))
y2 = int(input("Введите Y2: "))
#Точка
x3 = int(input("Введите X3: "))
y3 = int(input("Введите Y3: "))

mymath = MyMath(x1,y1,x2,y2,x3,y3)


print('Результат: {}'.format(mymath.result_function()))

class My1(object):
    """Class"""
    def __init__(self, x,y):
        """Constructor"""
        self.x = x
        self.y = y
    def more_x_or_y(self):
        if (self.x**3 > self.y**3):
            return x
        elif (self.x**3 < self.y**3):
            return y
        else:
            return x
    
    def __del__(self):
        print("Мусор удален!")

class MyMath(My1):
    """Class"""
    def result_function(self):
        f = (z + self.more_x_or_y())**3
        return f

x = int(input("Введите X: "))
y = int(input("Введите Y: "))
z = int(input("Введите Z: "))

my1 = MyMath(x,y)

print('Результат примера: {}'.format(my1.result_function()))

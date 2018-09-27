class Cub(object):
    """Class"""
    def __init__(self, x,y):
        """Constructor"""
        self.x = x
        self.y = y
    def proccesing_more(self):
        if (self.x**3 > self.y**3):
            return "X^3 > Y^3"
        elif (self.x**3 < self.y**3):
            return "Y^3 > X^3"
        else:
            return "Они равны!"

x = int(input("Введите X: "))
y = int(input("Введите Y: "))


cub = Cub(x,y)

print(cub.proccesing_more())

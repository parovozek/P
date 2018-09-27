import math as m
class VectorMy(object):
    """Class"""
    def __init__(self, x1,y1,x2 = 1,y2 = 2):
        """Constructor"""
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def math_length_vector(self):
        length = m.sqrt(self.x1**2 + self.y1**2 + self.x2**2 + self.y2**2)
        return round(length,2)
    
    def __del__(self):
        print("Мусор удален!")


x1 = int(input("Введите X1: "))
y1 = int(input("Введите Y1: "))

vector = VectorMy(x1,y1)
print('Длина вектора: {}'.format(vector.math_length_vector()))


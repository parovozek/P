import math as m
import colorama
colorama.init(strip=False)

class T1(object):
    def __init__(self, title, count_zachisl,count_vipusk,procent_vipusk):
        self.title = title
        self.count_zachisl = count_zachisl
        self.count_vipusk = count_vipusk
        self.procent_vipusk = procent_vipusk
    def __del__(self):
        print("Мусор удален!")
    
    def main_func(self):
        f = self.count_vipusk / self.count_zachisl
        return f

class T2(T1):
    def quality(self):
        f = self.procent_vipusk * self.main_func()
        return round(f,2)

x1 = str(input("Введите название заведения: "))
x2 = int(input("Введите количество студентов зачисленных на 1-й курс: "))
x3 = int(input("Введите количество выпусников: "))
x4 = int(input("Введите процент выпусников, которые работают по специальности (%): "))

my1 = T2(x1,x2,x3,x4)

print('Качество учебного заведения {color}{title}{endcolor} равняется: {color}{out}{endcolor}/100 баллов'.format(color = colorama.Fore.GREEN, endcolor = colorama.Fore.WHITE, title = x1, out = my1.quality()))

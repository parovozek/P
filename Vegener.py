#Шифр Виженера
from itertools import cycle #библиотека для управления бесконечным итерационым циклом 

LEN = 255 #длина таблицы 

def full_encode(value, key):
    ##Собираем каждый закодированный символ, путем анонимной функции, которая при каждой итерации прибавляет сопоставимый символ с ascii таблицей и введеным ключом пользователя, в строку
    return ''.join(map(lambda x: chr((ord(x[0]) + ord(x[1])) % LEN), zip(value, cycle(key)))) 
    ##Собираем каждый закодированный символ, путем анонимной функции, которая при каждой итерации вычитает сопоставимый символ с ascii таблицей и введеным ключом пользователя, с помощью чего расшифровывается строка
def full_decode(value, key):
    return ''.join(map(lambda x: chr((ord(x[0]) - ord(x[1]) + LEN) % LEN), zip(value, cycle(key))))

s = str(input("Введите текст для шифрования: ")).strip() 
k = str(input("Введите ключ шифрования: ")) #key для шифрования
shifr = full_encode(s,k)
print('\nSource: {source}\nЗашифрованное слово: {input}\nРаскодированное слово: {out}\n'.format(source=s, input = shifr, out = full_decode(shifr,k)))
#Шифр Цезаря
ALPHA = "".join(map(chr, range(ord(" "), ord("я") + 1)))
 
def encode(text, step):
    #Вовзращаем строку со сдвигом, с помощью количество итераций введенных пользователей, и формулы Цезаря(y = (x + k))
    return text.translate(
        str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))
 
def decode(text, step):
    return text.translate(
        #Декодируем строку путем сдвига в обратную сторону, который сопоставим количество проходов
        str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA))

s = str(input("Введите текст для шифрования: ")).strip()
n = int(input("Введите количество проходов: "))
shifr = encode(s,n) #шифруем строку 
print('\nSource: {source}\nЗашифрованное: {input}\nРаскодированное слово: {out}\n'.format(source=s, input = shifr, out = decode(shifr,n)))
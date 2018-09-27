import rsa
import colorama
colorama.init(strip=False)

(pubkey, privkey) = rsa.newkeys(512) #Создаем публичный и приватный 512-rsa ключ для шифрования и декодирования строки

message = str(input("Input something: ")) #Ввод
message_bytes = bytes(message, 'utf-8') #Переводим нашу строку в байты для шифрования ключом
# Шифруем строку
message_crypto = rsa.encrypt(message_bytes, pubkey)

#Расшифровываем строку
message_decode = rsa.decrypt(message_crypto, privkey)
#Вывод
print('{color1}Source:{endcolor1} {source}\n{color2}Зашифрованное слово:{endcolor2} {input}\n{color3}Раскодированное слово:{endcolor3} {out}\n'.format(color1 = colorama.Fore.GREEN,endcolor1= colorama.Fore.WHITE,color2 =colorama.Fore.LIGHTRED_EX,endcolor2=colorama.Fore.WHITE,color3 =colorama.Fore.LIGHTBLUE_EX,endcolor3=colorama.Fore.WHITE,source= message,input=message_crypto,out=message_decode))
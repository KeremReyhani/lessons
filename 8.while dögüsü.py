#while döngüsü: koşul devam ettikçe o işlemi devam ettirir.
number=1
while number<=10:
    print(number)
    number=number+1

#message=""
#while message !="quit":
#    message=input("quit yazana kadar devam et")
#    print(message)

#my_flag=True
#mesaj=""
#while my_flag:
#    mesaj=input("çıkmak için quit yazınız")
#    if mesaj=="quit":
#        my_flag=False
#    else:
#        print(mesaj)

sayı=1
while sayı<10:
    print(sayı)
    if sayı==5:
        break
    sayı=sayı+1

sayı=1
while sayı<10:
    sayı=sayı+1
    if sayı%2==0:
        continue #pas geç
    print(sayı)

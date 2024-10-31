#girilen sayının karesini gösteren fonksiyon
x=int(input("bir sayı giriniz"))
def func():
    print(x**2)
func()
                #veya
x=int(input("bir sayı giriniz"))
def func(x):
    return x**2
print(func(x))

#girilen iki sayının toplamını ve çarpımını lambda ile yaz
a=int(input("bir sayı giriniz: "))
b=int(input("bir sayı giriniz: "))
toplam= lambda a,b:a+b
çarpım= lambda a,b:a*b
print(f"toplam= {toplam(a,b)}")
print(f"çarpım= {çarpım(a,b)}")

#bir liste içindeki sayıların çarpımını gösteren fonksiyon
def çarpım(mylist):
    çrp=1
    for x in mylist:
        çrp=çrp*x
    return çrp
list1=[3, 5, 6, 10]
print(çarpım(list1))

#girilen bir sayının faktöriyelini gösteren fonksiyon yaz
def faktoriyel(a):
    if a==0:
        return 1
    else:
        return a*faktoriyel(a-1)
a=int(input("bir sayı giriniz: "))
print(faktoriyel(a))

#bir küpün alanını, çevresini ve hacmini hesapla
a=int(input("bir sayı giriniz: "))
çevre=12*a
alan=6*a**2
hacim=a**3
print(f"çevre= {çevre}, alan= {alan}, hacim= {hacim}")
                            #yada
a=int(input("bir kenar uzunluğu giriniz: "))
def çevre(a):
    return 12*a
def alan(a):
    return 6*a**2
def hacim(a):
    return a**3
print(f"çevre= {çevre(a)}, alan= {alan(a)}, hacim= {hacim(a)}")


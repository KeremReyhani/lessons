#alan ve çevreyi ondalıklı olarak bul
r=5
pi=3.14159
çevre=2*pi*r
alan=pi*r**2
print("çevre=", çevre)
print("alan=", alan)   #veya print(pi*(pow(r,2)))
print("çevre=", round(çevre))
print("alan=", round(alan))

import math #matematik kütüphanesinden bulur
print(2*math.pi*r)

#x tek mi çift mi yazdır
x=21
if(x%2==0):
    print("x bir çift sayıdır")
else:
    print("x bir tek sayıdır")

#|4-7|*(4+7)=?
print(abs(4-7)*(4+7))

isim=" kerem"
print("Benim adım" + isim)
print("Benim adım {}".format(isim))
print(f"Benim adım {isim}")

x="50"
y=100
print(int(x)-y)

soru=input("isminiz nedir?")
print(soru.upper())
print(soru.lower())

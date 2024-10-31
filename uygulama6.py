#takımlar=["beşiktaş", "fenerbahçe", "galatasaray", "trabzonspor", "hatayspor"] trabzonspor hariç diğerlerini while ve for loop kullanarak yaz
takımlar=["beşiktaş", "fenerbahçe", "galatasaray", "trabzonspor", "hatayspor"]
x=0
while (x<len(takımlar)):
    k=takımlar[x]
    x=x+1
    if k=="trabzonspor":
        continue
    print(k)

for y in takımlar:
    if y=="trabzonspor":
        continue
    print(y)

#girilen 2 sayı arasındaki çift sayıları yaz
sayı1=int(input("bir sayı giriniz:"))
sayı2=int(input("bir sayı giriniz:"))
for ç in range(sayı1, sayı2):
    if ç%2!=0:
        continue
    else:
        print(ç)


#while dögüsü ile 1 ile 100 arasındaki sayı tahminlerini yapabileceğiniz bir program yaz
#import random
#xnum=random.randint(1,100)
#print(xnum)
import random
xnum=random.randint(1,100)

num=int(input("lütfen 1 ile 100 arasında bir sayı girin:"))
while num!=xnum:
    if num<xnum:
        print(f"{num} daha büyük bir sayı giriniz")
        num=int(input())
    else:
        print(f"{num} daha küçük bir sayı giriniz")
        num = int(input())
print(f"tebrikler {num} yakaladınız")

#celciuses=[20, 25, 30, 35] derecelerini kelvin ve fahrenheit olarak 2 farklı listede göster
#K=C+273                 F=C*9/5+32
celciuses=[20, 25, 30, 35]
kelvin=[]
fahrenheit=[]
for c in celciuses:
    k=c+273
    kelvin.append(k)
    f=c*9/5+32
    fahrenheit.append(f)
print(kelvin)
print(fahrenheit)

#bir sayı gir ve o sayı ve öncekilerin toplamını yaz
sayı=int(input("bir sayı giriniz"))
if sayı<0:
    print("pozitif bir sayı giriniz")
else:
    sum=0
    while sayı>0:
        sum= sum + sayı
        sayı = sayı-1
print("toplam sayı:", sum)
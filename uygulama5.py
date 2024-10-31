#girilen sayı tek mi çift mi
sayı=int(input("bir sayı giriniz"))
if sayı%2==0:
    print(f"{sayı} sayısı çifttir")
else:
    print(f"{sayı} sayısı tektir")

#x=10
#y=5
#if x>y:
#   print(f"{x} sayısı {y}'den büyüktür ")
#ifadesinin tek satır formunu yazın, else yapısıyla tine tek satırda yazın
x=10
y=15
if x>y:print(f"{x} sayısı {y}'den büyüktür ")
print(f"{x} sayısı {y}'den büyüktür ") if x>y else print(f"{x} sayısı {y}'den küçüktür ")

#girilen sayının faktöriyelini bul
num=int(input("bir sayı giriniz"))
faktöriyel=1
if num<0:
    print(f"{num} sayısı negatif")
elif num==0:
    print(f"{num}! = 1")
else:
    for x in range(1,num+1):
        faktöriyel=faktöriyel*x
    print(f"{num}! = {faktöriyel}")

#notes={"ahmet":58, "mehmet":76, "ebru":44, "pınar":90} 50 üzeri geçer yaz
notes={"ahmet":58, "mehmet":76, "ebru":44, "pınar":90}
for key, value in notes.items():
    if value>=50:
        print(f"{key}: geçti")
    else:
        print(f"{key}: kaldı")



age=18
if age>=18:
    print("oy kullanabilirsiniz")

my_list=["a", "b", "c"]
if "a" in my_list:
    print("evet")

age=16
if age>=18:
    print("oy kullanabilirsiniz")
else:
    print("oy kullanamazsınız")

age=15
if age<=2:
    print("%60 indirimli")
elif age>=10:
    print("%30 indirimli")
else:
    print("indirim yok")

age=int(input("yaşınızı giriniz: "))
if age<0:
    age=0
    print("negatif sayı 0'a çevrildi")
elif age==0:
    print("lütfen başka sayı giriniz")
elif age<18:
    print("oy kullanamazsın")
else:
    print("oy kullanabilirsiniz")

my_condition=None
if my_condition:
    print("koşul doğru")
else:
    print("koşul yanlış")



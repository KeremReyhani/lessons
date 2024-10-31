import math
print(math.prod((2,6,8))) # 2*6*8
print(math.sqrt(15)) #kök içine alır
print(math.isqrt(15)) #kökün tam kısmı


#THE WALRUS OPERATOR(:=) : bir değeri atayabiliyor ve return edebiliyoruz.
print(name:="kerem")

if (x:=40)>20:
    print(f"{x} 20 den büyüktür")

mylist=list()
#while True:
#    entry=input("listeye ekle: ")
#    if entry=="exit":
#        break
#    mylist.append(entry)
#print(mylist)

while (entry:=input("listeye ekle: ")) != "exit":
    mylist.append(entry)
print(mylist)


#F-STRING DEBUGGER
name="kerem"
print(f"{name=}")



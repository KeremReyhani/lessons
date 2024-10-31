#boolen veri tipleri ture ve false diye cevap verir. True=1 false=0
bool1=True
bool2=False
print(type(bool1))
print(type(bool2))

a=2
b=True
print(a>b)

c=0
d=False
print(c==d)

age=18
bool3=age>=26
print(bool3)
#  != ifadesi eşit deği anlamında
print(5!=6)

x=["ahmet", "mehmet"]
y=["ahmet", "mehmet"]
print(x==y)
print(x is y)  # is eşittir anlamına gelir ama hafızada iki farklı konumda tutuyorsa eşit olmaz

x=5
y=5
print(x==y)
print(x is y)

print(32>28 and 17<14) #hepsi doğru olmalı
print(32>28 or 17<14) #en az biri doğru olmalı
print(not False)
"""
Boş bir  student class oluştur ve setattr metodunu kullanarak isim ve yaş özelliklerini dinamik olarak ekle.
"""
class Student:
    pass

std1=Student()
setattr(std1, "name", "Kerem")
std2=Student()
setattr(std2, "age", 18)

print(std1)
print(std2)
print(std1.name)
print(std2.age)

print()
print()

"""
init metoduyla boş bir  student class oluştur herhangi bir nesneyi güncelle ve del kullanarak sil sonra delattr kullan
"""

class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"İsim: {self.name} - Yaş: {self.age}"
std1=Student("Kerem", 18)
print(std1.age)
std1.age=20
print(std1.age)

print(std1)
print(vars(std1))

del std1.age
print(vars(std1))

delattr(std1, "name")
print(vars(std1))

print()

std3=Student("Yusuf", 36)
std4=std3
del std3
print(std4)

print()
print()

"""
selvi olarak kendi sel parametremizi oluşturalım
"""
class Student:
    def __init__(selvi, name, age):
        selvi.name=name
        selvi.age=age
    def __str__(selvi):
        return f"İsim: {selvi.name} - Yaş: {selvi.age}"

std1=Student("Ege", 26)
print(std1)

print()
print()

"""
__mro__ metoduna örnek yap (method resolution order)
"""
class A():
    pass
class B(A):
    pass
class C(B):
    pass
class D:
    pass
class E(D, C):
    pass

print(E.__mro__)
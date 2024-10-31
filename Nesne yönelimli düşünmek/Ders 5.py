#encapsulation: bir class içinde bulunan metod ve değişkenlerin erişimini kısıtlamaktır.
class Employee:
    def __init__(self, name, age):
        self.__name=name # __: korumaya alır
        self.age=age

    def get_name(self): #ismi alır
            return self.__name
    def set_name(self, name): #attribute'yi değiştirir
            self.__name=name

employee1=Employee("Kerm", 18)
employee2=Employee("Aliy", 52)
"""
print(f"İsim: {employee1.name} - Yaş: {employee1.age}")
print(f"İsim: {employee2.name} - Yaş: {employee2.age}")
bunlar değişir
"""
print(f"İsim: {employee1.get_name()} - Yaş: {employee1.age}")
print(f"İsim: {employee2.get_name()} - Yaş: {employee2.age}")

employee1.set_name("Kerem")
employee2.set_name("Ali")
print(f"İsim: {employee1.get_name()} - Yaş: {employee1.age}")
print(f"İsim: {employee2.get_name()} - Yaş: {employee2.age}")
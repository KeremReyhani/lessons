#dekoratör:fonksiyonu geliştirmek için
class Student:

    def __init__(self, name, surname, age, grades):
        self.name=name
        self.surname=surname;
        self.age=age
        self.grades=grades

    def avarage(self):
        return sum(self.grades)/len(self.grades)
    @property
    def fullname(self):
        return f"{self.name} {self.surname}"
student1=Student("kerem", "reyhani", 18, [80, 90, 100])
student1.name="KEREM"
student1.surname="REYHANİ"
print(student1.name)
print(student1.surname)
print(student1.fullname)
print(student1.avarage())
#Abstract - Soyut class: kullanacağımız fonksiyonları önceden tanımlamamızı sağlar
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.name=name

    @abstractmethod #artık bu class'tan nesne oluşturulamaz
    def salary(self):
        return 5000

class Engineer(Employee):
    def __init__(self, name, title):
        super().__init__(name)
        self.title=title
    def salary(self):
        return 10000

    def __str__(self):
        return f"İsim: {self.name} - Maaş: {self.salary()}"

"""
emp1=Employee("Kerem")
print(emp1.name)
print(emp1.salary())

eng1=Engineer("Yusuf", "Engineer")
print(eng1.name)
print(eng1.salary())
"""

eng1=Engineer("Ege", "Engineer")
print(eng1.name)
print(eng1.salary())


print(isinstance(eng1, Employee))

#person parent class name, surname, age, properties __str__dunder method name, surname ve str(age)
#employee child class salary property, __str__dunder method + salary
class person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age
    def __str__(self):
        return self.name + " " + self.surname + " " + str(self.age)
person1=person("kerem", "reyhani", 18)
print(person1.__str__())

class employee(person):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age)
        self.salary=salary

    def __str__(self):
        return super().__str__() + " " + str(self.salary)

employee1=employee("kerem", "reyhani", 26, 15000)
print(employee1.salary)
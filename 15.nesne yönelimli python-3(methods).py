#instances metotları parametre olarak self alır, class metotları cls key wordunu alır
class students:
    school_name="x lisesi"
    number_of_students=0

    def __init__(self, name, age, grades):
        self.name=name
        self.age=age
        self.grades=grades
        students.number_of_students+=1
    def avarage(self):
        return sum(self.grades)/len(self.grades)
    @classmethod                                    #metot veya değişken değiştirebiliriz
    def display_school_name(cls, name_of_school):
        cls.school_name=name_of_school
students.display_school_name("y lisesi")

student1=students("kerem", 18, [14, 26, 72, 84])
student2=students("yusuf", 14, [20, 40, 70, 90])

student1.school_name="z lisesi"

print(students.school_name)
print(student1.school_name)
print(student2.school_name)



class students:
    school_name="x lisesi"
    number_of_students=0

    def __init__(self, name, age, grades):
        self.name=name
        self.age=age
        self.grades=grades
        students.number_of_students+=1
    def avarage(self):
        return sum(self.grades)/len(self.grades)
    @staticmethod                                             #class'ın herhangi bir verisine etki etmez. ekleme falan yapabilir
    def statik():
        return f"sadece bu mesajı yazdır"

student1=students("kerem", 18, [14, 26, 72, 84])
student2=students("yusuf", 14, [20, 40, 70, 90])

print(students.statik())
print(student1.statik())









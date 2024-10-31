#ortak özellikleri türetme
class Student:

    def __init__(self, name, age, grades):
        self.name=name
        self.age=age
        self.grades=grades
    def avarage(self):
        return sum(self.grades)/len(self.grades)


student1=Student("kerem", 18, [14, 26, 72, 84])
student2=Student("yusuf", 14, [20, 40, 70, 90])


class UniversityStudent(Student):
    pass
u_student_1=UniversityStudent("arin", 22, [10, 20, 30])
print(u_student_1.age)
print(u_student_1.name)
print(u_student_1.avarage())
print(help(UniversityStudent))


class Student:

    def __init__(self, name, age, grades):
        self.name=name
        self.age=age
        self.grades=grades
    def avarage(self):
        return sum(self.grades)/len(self.grades)

student1=Student("kerem", 18, [14, 26, 72, 84])
student2=Student("yusuf", 14, [20, 40, 70, 90])

class UniversityStudent(Student):
    def __init__(self, name, age, grades, university):
        super().__init__(name, age, grades)
        self.university=university
u_student_2=UniversityStudent("kerem", 18, [80, 90, 100],  "YTU")
print(u_student_2.university)
print(u_student_2.avarage())




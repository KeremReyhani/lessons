#instances nesne olarak düşünülebilir (her bir student)
class students:
    schoolname="x lisesi"
    number_of_students=0

    def __init__(self, name, age, grades):
        self.name=name
        self.age=age
        self.grades=grades
        students.number_of_students+=1
    def avarage(self):
        return sum(self.grades)/len(self.grades)
    def school_name(self):
        return f"okulumuzun adı {self.schoolname}"

print(students.number_of_students)
student1=students("kerem", 18, [14, 26, 72, 84])
student2=students("yusuf", 14, [20, 40, 70, 90])
print(students.number_of_students)

print(student1.avarage())
print(student1.name)
print(student1.schoolname)
print(students.schoolname)
print(student1.school_name())

print(student2.__dict__)
print(students.__dict__)


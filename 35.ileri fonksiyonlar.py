#FIRST CLASSS FONCTIONS: bir değişkene atanan fonksiyonlar
def summation(x,y):
    return x+y

result=summation
print(type(summation))
print(type(result))
print(summation)
print(result)

print(result(10,12))


#HIGHER ORDER FONCTIONS: başka bir fonksiyonu kendisine argüman alan fonksiyon

def summation(arr1, func):
    total=0
    for i in arr1:
        total+=func(i)
    return total

def squared(x):
    return x**2
def cubed(y):
    return y**3

print(summation([1,2,3], squared)) # 1+4+9
print(summation([2,1,4], cubed)) # 8+1+64


#RETURN FUNCTION: bir fonksiyondan başka bir fonksiyonu return eder

def say_name(name):
    def my_name():
        print(f"benim adım {name}")
    return my_name

name_1=say_name("kerem")
name_1()


def employee(name):
    def salary(lira):
        print(f"benim adım {name} ve maaşım {lira}")
    return salary
emp1=employee("kerem")
emp1(200)
emp1(500)


#NESTED FONCTIONS: iç içe fonksiyonlar

from random import choice

def my_team(team):
    def get_title():
        message=choice(("Şampiyon ","Vasat ", "Küme "))
        return message
    result=get_title()+team
    return result
print(my_team("Beşiktaş"))


#CLOSURE: bir fonksiyonun kendi kapsamı dışında değişken kullanması

def parent_func(name):
    the_name=name
    def inner_func():
        print(f"benim adım {the_name}")
    return inner_func()

parent_func("kerem")
# *args   parçalara ayırıyor (tuple olarak döner)
def print_names(name1, name2, name3):
    print(name1,name2,name3)
names=["ahmet", "mehmet", "ayşe"]
print_names(*names)

def print_names(*args):
    for name in args:
        print(name)
print_names("ahmet", "mehmet", "ayşe", "fatma")

def print_names(name1, name2, *args):
    print(name1, name2, args)

print_names("ahmet", "mehmet", "ayşe", "fatma", "hakan")



def sum_numbers(*args):
    total=0
    for num in args:
        total+=num
    return total
print(sum_numbers(4,7))
print(sum_numbers(9,12,23,35))



# **kwargs (dictionary olarak döner)
def fav_pro(**kwargs):
    for name,program in kwargs.items():
        print(f"{name}: {program}")
fav_pro(kerem="python", yusuf="c++", ege="java")
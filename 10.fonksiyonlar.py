def func():      #def: fonksiyon için key word, func:fonksiyonun ismi
    print("hello world")
func()

def func():
    print("hello world")
print(func)

def my_function(username): #username: parametre
    print(f"hello {username}")
my_function("kerem") #kerem: argüman
my_function("ali")

def my_function(username="yusuf"):
    print(f"hello {username}")
my_function()

def my_function(username="yusuf"):
    print(f"hello {username}")
my_function()
my_function("aliye")

def func(kullanıcıadı, yaş=18):
    print(f"merhaba {kullanıcıadı}, {yaş} yaşındasın")
func("kerem")


def func1():
    return 5+10

def func2():
    print(6+10)

func1()
func2()


def func1():
    return 5+10

def func2():
    print(6+10)

result1=func1()
result2=func2()
print(f"sonuç1, {result1}")
print(f"sonuç2, {result2}")


def func():
    pass #hiçbir işlem yapmaz
func()

name="kerem"                                                        #global değişkenler(name ve age)
age=18
def hello():
    name="reyhani"
    age=20                                                          #aynı fonksiyonun içindeki değişkenler local değişkenlerdir(name ve age)
    message=f"benim adım {name} ve {age} yaşındayım."
    print(message)
hello()
print(name)
print(age)


x="global"
def myfunc():
    x="local"
    return x
print(x)
print(myfunc())

k="global level"
def enclosing():
    k="enclosing level"
    def innerfunc():
        k="local level"
        print(k)
    innerfunc()
enclosing()
#print sıralaması LEGB (local-enclosing-global-built-in)


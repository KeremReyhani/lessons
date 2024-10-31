#hazır fonksiyonlar
mylist=[1, 4, 7, 3, 9, 4]
print(len(mylist))

myset=set(mylist)
print(myset)
print(sum(myset))



def func(x):
    return x**2
print(func(5))

y=lambda a:a**2
print(y(6))

y=lambda m,n:m+n
print(y(20,30))

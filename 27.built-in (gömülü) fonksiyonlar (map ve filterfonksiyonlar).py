def sqrt(x):
    return x**2
print(sqrt(4))
                                        #lambda başka fonksiyonun parametresi olacak şekilde kullanılır.
sqrt2= lambda x:x**2
print(sqrt2(4))

sum= lambda x,y:x+y
print(sum(5,6))


#map(function, iterable) iterable: yenilenebilir.

list1=[1,2,3,4,5]
print(list(map(lambda x:x**2, list1)))

friends=["kerem", "ege", "yusuf"]
print(list(map(lambda friend:friend.upper(), friends)))


#filter(function, iterable) iterable: yenilenebilir.

num=[1,2,3,4,5,6]
print(list(filter(lambda x:x>3, num)))

friends=["mustafa", "ali", "kerem"]
print(list(filter(lambda name:len(name)>5, friends)))
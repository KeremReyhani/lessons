#iterable metodlar iterator nesneleri barındıran konteynerlerdir. iterator'e ulaşmak için iter metodu kullanılır. iteratorler aynı zamanda iterable elemanlardır.
friends=["kerem", "ege", "yusuf"]
print(type(friends))

i_friends=iter(friends)

print(type(i_friends))
print(dir(i_friends))

print(i_friends)
print(next(i_friends))
print(next(i_friends))
print(next(i_friends))
print(list(i_friends))

i_friends2=iter(friends)
print(list(i_friends2))


friends=["kerem", "ege", "yusuf"]
i_friends=iter(friends)
while True:
    try:
        print(next(i_friends))
    except StopIteration:
        break


kare=map(lambda x:x*x, [2,5,7])
print(next(kare))
print(next(kare))
print(next(kare))



class myEvenNumbers:
    def __init__(self, start, end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start>self.end:
            raise StopIteration
        else:
            current=self.start
        if current %2 != 0:
            self.start+=1
            return next(self)
        else:
            self.start += 2
            return current
numbers=myEvenNumbers(3,17)
for number in numbers:
    print(number)


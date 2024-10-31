#numbers=[1,2,3,4,5]   friends=["kerem","yusuf","ege"]    listeleri ile çalışacak for loop yapısı oluştur.
numbers=[1,2,3,4,5]
friends=["kerem","yusuf","ege"]
def my_for_loop(my_iterable):
    my_iterator=iter(my_iterable)
    while True:
        try:
            print(next(my_iterator))
        except StopIteration:
            break
my_for_loop(numbers)
my_for_loop(friends)

#0 ile 10 arasındaki sayıların küplerini göstermeyi iterator sınıfı yardımıyla yapalım.
class CubeNumbers:
    def __init__(self, start, end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<=self.end:
            result=self.start**3
            self.start+=1
            return result
        else:
            raise StopIteration
cube=CubeNumbers(0,5)
print(next(cube))
print(next(cube))
print(next(cube))
print(next(cube))
print(next(cube))
print(next(cube))


#0 ile 10 arasındaki sayıların küplerini göstermeyi generator expression ile yapalım.
cubed=(x**3 for x in range(0,5))
print(type(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))

#belirli bir sayıya kadar fibonacci sayılarını yaz.
def fibo(limit):
    x=0
    y=1
    while x<limit:
        yield x
        x,y=y,x+y
my_fibo=fibo(1000)
for fib in my_fibo:
    print(fib)
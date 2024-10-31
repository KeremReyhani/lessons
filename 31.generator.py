#işlemleri uygularken durdurabileceğimiz veya tekrer çalıştırabileceğimiz fonksiyonlara denir.
#generator iteratorün alt kümesidir
def odds(limit):
    for odd in range(1, limit+1, 2):
        yield odd    #yield elemanı tutar
print(odds)
print(odds(15))

my_odds=odds(15)
print(next(my_odds))


limit=15
my_odds2=(odd for odd in range(1, limit+1, 2))
print(my_odds2)
print(next(my_odds2))
print(next(my_odds2))
print(next(my_odds2))
print(next(my_odds2))

list1=["a","b","c","d"]
my_gen=(char for char in list1)
print(my_gen)
print(next(my_gen))
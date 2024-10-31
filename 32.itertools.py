# sıklıklıkla kullanılan iterator fonksiyonlardan ve onların kombinasyonlarından oluşur.

# COUNT FONKSİYONU: belirlediğimiz sayıda ve belirlediğimiz kadar eleman dönüşü yapar.

# from itertools import count
# counter=count(10, 2) #2 artış miktarı
# print(next(counter))
# print(next(counter))
# print(next(counter))

# for i in counter:
#    print(i)

# from itertools import count, islice
# counter=islice(count(10,4),5)
# for i in counter:
#    print(i)


# cycle: sonsuz geri dönüş yapar
# from itertools import cycle
# cities=["istanbul", "ankara", "hatay"]
# cycled=cycle(cities)
# print(next(cycled))
# print(next(cycled))
# print(next(cycled))
# print(next(cycled))


# REPEAT: argümanı sonsuz sayıda geri döner
#from itertools import repeat
#repeated=repeat(10, 5) #5 kaç kere yazdıracağını gösterir.
#print(next(repeated))
#print(next(repeated))
#print(next(repeated))
#print(list(map(pow, range(10), repeat(3))))


#CHAIN: bağlar
#from itertools import chain
#list_1=[1,2,3,4,5]
#list_2=["İstanbul", "Ankara", "Hatay"]
#list_3=[True, False]
#new_list=list(chain(list_1, list_2, list_3))
#print(new_list)

#COMPRESS
from itertools import compress
data=["istanbul", "izmir", "ankara", "çanakkale", "eskişehir", "bursa"]
selectors=[True, False, True, False, True, False]
print(list(compress(data, selectors)))
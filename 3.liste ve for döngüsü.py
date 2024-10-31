şehirler=["istanbul", "hatay", "eskişehir", "adana", "mardin"]
print(şehirler[0])
print(şehirler[2])
print(şehirler[-1])
print(şehirler[0:2])
print(len(şehirler))
şehirler[4] = "ankara"
print(şehirler)
şehirler.append("bursa")
print(şehirler)
şehirler.insert(2, "çanakkale") #belirli bir yere eklemek için
print(şehirler)
del şehirler[4] #silinen elemana ulaşamayız
print(şehirler)
şehirler.pop() #son elemanı siler
print(şehirler)
şehirler2=şehirler.pop() #silinen elemanı başka yere yazdırır
print(şehirler2)
şehirler.remove("çanakkale")
print(şehirler)


şehirler=["istanbul", "hatay", "eskişehir", "adana", "ankara"]
print(şehirler)
şehirler.sort()
print(şehirler)
şehirler.sort(reverse=True)
print(şehirler)
şehirler=["istanbul", "hatay", "eskişehir", "adana", "ankara"]
print(şehirler)
print(sorted(şehirler)) #yeni hali kaydetmez sonrakinde eskiye döner
print(şehirler)


sayılar=[36, 47, 18, 77]
print(min(sayılar))
print(max(sayılar))
print(sum(sayılar))






cities=["Londra", "New York", "Barselona", "Roma"]
print(cities.index("Roma")) #kaçıncı sırada
print("Berlin" in cities)
print("Londra" in cities)

for city in cities:
    print(city)
for x in cities:
    print("Gezilen Yerler:" + x)
    print("yer kalmadı")


str_cities = "madrid, berlin, kiev"
my_list=str_cities.split(", ")
print(my_list)
str_email="kerem.reyhani@gmail.com"
my_list2=str_email.split("@")
print(my_list2)


for number in range(1,10):
    print(number)


for number in range(1,20,3): #artış miktarı
    print(number)

numbers=list(range(1,20,3))
print(numbers)

sayılar2=[sayı for sayı in range(1,11)]
print(sayılar2)
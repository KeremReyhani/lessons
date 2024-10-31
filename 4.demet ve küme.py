başkentler=("ankara", "madrid", "londra", "washnington")   #demet(tuple) normal parantezle()gösterilir.
print(type(başkentler))
print(len(başkentler))
print(başkentler[1])
print(başkentler[1:3])
for başkent in başkentler:
    print(başkent)




şehirler={"istanbul", "izmir", "ankara", "hatay"}
print(type(şehirler))
print(şehirler)
şehirler={"istanbul", "izmir", "ankara", "hatay", "istanbul"}
print(şehirler)
#print(şehirler[1]) #set elemanlarının index numarası yok
şehirler.add("eskişehir")
print(şehirler)
şehirler.update(["adana", "mersin"])
print(şehirler)
şehirler.remove("adana") #olmayan elemanı kaldırmayı çalışırsak hata verir
print(şehirler)
şehirler.discard("izmir") #olmayan elemanı kaldırmayı çalışırsak hata vermez
print(şehirler)
şehirler.clear()
print(şehirler)
#list1=[14,12,26,32]        list2=[4,5,2,1]    liste elemanlarının toplamlarını ve çarpımlarını liste içinde göster
list1=[14,12,26,32]
list2=[4,5,2,1]
print(list(map(lambda x,y:x+y, list1, list2)))
print(list(map(lambda x,y:x*y, list1, list2)))

#list comprehension yöntemi ile fahrenheit F=[99,108,176,204] derecelerini Celcius derecelerine çevir. C=(F-32)*(5/9)
Fh=[99,108,176,204]
print([(F-32)*(5/9) for F in Fh])

#list_1=["mustafa", "ahmet", "arin", "cem", "ayşegül", "hakan"] 4 harften uzunlarla yeni bir liste
list_1=["mustafa", "ahmet", "arin", "cem", "ayşegül", "hakan"]
print(list(filter(lambda name:len(name)>4, list_1)))

#all(iterable) hepsi true olmalı
list1=[2,7,1,13]
print(all(list1)) #all fonksiyonu 0 hariç true.

list2=[]
print(all(list2))

dict1={1:True, 2:False}
print(all(dict1))   #önemli olan key değeri

dict2={1:True, 0:False}
print(all(dict2))



#any(iterable) en az biri true olmalı

list1=[0, False, False, 7]
print(any(list1))

list2=[]
print(any(list2))

dict1={1:True, 2:False}
print(any(dict1))   #önemli olan key değeri

dict2={1:True, 0:False}
print(any(dict2))


friends=["ali", "ayşe", "ahmet", "ayhan"]
print(all(friend[0] =="a" for friend in friends))

friends=["ali", "ayşe", "ahmet", "ayhan", "mehmet"]
print(all(friend[0] =="a" for friend in friends))

friends=["ali", "ayşe", "ahmet", "ayhan", "mehmet"]
print(any(friend[0] =="a" for friend in friends))
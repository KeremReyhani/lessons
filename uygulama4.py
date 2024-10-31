#boş liste, tuple, set ve dictionary oluştur
my_list1=[]
my_list2=list()
print(type(my_list1))
print(type(my_list2))
print(my_list1)
print(my_list2)

tuple1=()
tuple2=tuple()
print(type(tuple1))
print(type(tuple2))
print(tuple1)
print(tuple2)

set1={}   #böyle boş set oluşturulamaz
set2=set()
print(type(set1))
print(type(set2))
print(set1)
print(set2)

dict1={}
dict2=dict()
print(type(dict1))
print(type(dict2))
print(dict1)
print(dict2)


#değeri sayı olan 3 elemanlı dict oluştur, 2.sayıyı ve sayıların ortalamasını yaz
dictionary={"yaş":18, "boy":182, "kilo":73}
print(dictionary["boy"])
print(sum(dictionary.values())/len(dictionary))

#my_dict={"odd_numbers":[1, 2, 3]} tüm elemanların karesini al ve aynı dictionary'yi update et
my_dict={"odd_numbers":[1, 2, 3]}
my_dict["odd_numbers"]=[my_dict["odd_numbers"][0]**2, my_dict["odd_numbers"][1]**2, my_dict["odd_numbers"][2]**2]
print(my_dict)


#my_dict2={"even_numbers":[2, 4, 6, 8, 10, 12, 14, 16]} tüm elemanların karesini al ve aynı dictionary'yi update et (for döngüsü ile)
my_dict2={"even_numbers":[2, 4, 6, 8, 10, 12, 14, 16]}
for x in my_dict2.values():
    my_list=[]
    for y in x:
            my_list.append(y**2)
my_dict2["even_numbers"]=my_list
print(my_dict2)


#my_friends={"ali":28, "mahmut":46, "ebru":34} key'lerden liste oluştur, value'lerden liste oluştur, value'ler toplamını yaz
my_friends={"ali":28, "mahmut":46, "ebru":34}
my_list_key=list(my_friends.keys())
my_list_value=list(my_friends.values())
print(my_list_key)
print(my_list_value)
print(sum(my_friends.values()))


#dictionary comprehension ile 1'den 10'a kadar olan sayılar key, kareleri value olacak şekilde tek satırda oluştur
numbers={x:x**2 for x in range(1,11)}
print(numbers)
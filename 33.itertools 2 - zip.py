import operator

list_1=[1,2,3,4]
list_2=["a", "b", "c", "d"]

zip_1=zip(list_1, list_2)
zip_2=zip(list_1, list_2)
print(list(zip_1))
print(dict(zip_2))

list_1=[1,2,3,4,5,6,7]
list_2=["a", "b", "c", "d"]

zip_1=zip(list_2, list_1)
print(list(zip_1))


students=["ahmet", "mehmet", "fatma"]
notes=[78,69,74]
for st, no in zip(students,notes):
    print(f"student: {st}, note: {no}")


#from itertools import zip_longest
#list_1=[1,2,3,4,5,6,7]
#list_2=["istanbul", "ankara"]
#zip_1=zip_longest(list_1, list_2)
#print(list(zip_1))
#zip_1=zip_longest(list_1, list_2, fillvalue="CITY")
#print(list(zip_1))


#from itertools import filterfalse   #yanlışları yazar.
#list_1=list(filterfalse(lambda x:x>5, [1,7,8,9,12,2]))
#print(list_1)



#from itertools import dropwhile #sadece yazmaması gereken ilk şeyi yazmaz.
#list_1=list(dropwhile(lambda x:x<5, [1,7,8,9,12,2]))
#print(list_1)


from itertools import accumulate
list_1=[3,51,2,10,1,4]
new_list=list(accumulate(list_1))
print(new_list)

list_1=[3,51,2,10,53,4]
new_list=list(accumulate(list_1, max))
print(new_list)

list_1=[3,51,2,10,1,4]
new_list=list(accumulate(list_1, operator.mul))
print(new_list)

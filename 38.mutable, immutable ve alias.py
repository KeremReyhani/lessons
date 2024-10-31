#MUTABLE: oluşturulduktan değiştirilebilen nesneler için kullanılır.
#IMMUTABLE: oluşturulduktan değiştirilemeyen nesneler için kullanılır.
#ALIAS: bir değişkenin başka değişkene atanması


#                                   MUTABLE: list, set, dictionary
"""friends=["kerem", "ege", "yusuf"]
print(id(friends)) # id'leri aynı olan ifadeler hafızada aynı nesneyi tutar.
friends2=friends
print(id(friends2))
friends.append("umut")
friends3=friends2
print(id(friends3))"""


#                                   IMMUTABLE: string, integer, tuple, float
"""name="kerem"
print(id(name))
name="kerem"
print(id(name))
name="yusuf"
print(id(name))"""


#                                   ALIAS
"""nums=[5,8]
nums2=nums
nums.append(9)
print(nums)
print(id(nums))
print(nums2)
print(id(nums2))"""

"""num=10
num2=num
num+=10
print(num)
print(id(num))
print(num2)
print(id(num2))
# num ve num2 ilk başta birbirinin elias'ı değişiklik yaptıktan sonra değil"""

my_list=[]
for i in range(5):
    my_list.append("test")
    print(my_list)
    print(id(my_list))

print()
print()
print()
print()
print()

my_list=[]
for i in range(5):
    my_list.append(["kerem", "reyhani"])
    print(my_list)
    print(id(my_list[i]))

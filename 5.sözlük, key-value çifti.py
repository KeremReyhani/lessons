monster_1={"name":"guru", "power":90, "color":"red"}  #önce key değeri sonra value
print(type(monster_1))
print(monster_1)
print(monster_1["name"])
monster_1["position"]=100
print(monster_1)
print(monster_1["position"])
print(monster_1.get("power"))
print(monster_1.get("boy")) #olmayan eleman yazarsan hata vermez
monster_1["tall"]="210 cm"
print(monster_1)
monster_1.update({"name":"GURU", "power":120, "age":1689})
print(monster_1)
del monster_1["color"]
print(monster_1)
poplan=monster_1.pop("power") #geri getirilebilir
print(monster_1)
print(poplan)
print(len(monster_1))
print(monster_1.keys())
print(monster_1.values())
print(monster_1.items())
for key in monster_1:
    print(key)
for value in monster_1.values():
    print(value)
monster_1.clear()
print(monster_1)

my_friends=[
    {"name":"kerem", "age":18},
    {"name":"yusuf", "age":14}
]
print(my_friends[0]["age"])

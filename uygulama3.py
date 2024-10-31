#new_tuple=("izmir", [18, "kerem"], (2, 4, 6), 100) print kerem, print 6
new_tuple=("izmir", [18, "kerem"], (2, 4, 6), 100)
print(new_tuple[1][1])
print(new_tuple[2][2])


new_tuple=("istanbul") #tek elemanlı tuple string olur (sona virgül atarsan düzelir)
print(type(new_tuple))


#new_tuple=(4, 8, [1, 20]) 4ü 50ye 1i 100e çevir
new_tuple=(4, 8, [1, 20])
new_tuple[2][0]=100 #tuple'ın içinde liste varsa değişebilir yoksa değişmez
print(new_tuple)


#cities=("istanbul", "ankara", "izmir") izmir ve balıkesir liste elemanı mı
cities=("istanbul", "ankara", "izmir")
print("izmir" in cities)
print("balıkesir" in cities)


#new_tuple=("5", "izmir", 28, "ankara", "5", "izmir") aynı değerleri teke indir
new_tuple=("5", "izmir", 28, "ankara", "5", "izmir")
new_set=set(new_tuple)
print(new_set)
                                            #yada
new_tuple2=tuple(set(new_tuple))
print(new_tuple2)


#new_set={"ahmet", "mehmet", "ayşe", "fatma"} ismini ekleyip listeye çevir
new_set={"ahmet", "mehmet", "ayşe", "fatma"}
new_set.add("kerem")
new_list=list(new_set)
print(new_list)
print(type(new_list))


#dsjklfsadkllsakgjklhjdfkhsafşlsafklsşdh tüm harfleri teke indir ve set şeklinde yaz
new_string="dsjklfsadkllsakgjklhjdfkhsafşlsafklsşdh"
new_set2=set(new_string)
print(new_set2)
                                                        #yada
new_set2={harf for harf in new_string}
print(new_set2)

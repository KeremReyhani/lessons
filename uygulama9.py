with open("data3.txt", "r") as my_file:
    print(my_file.read())
    print(my_file.read(5)) #ilkinden sonra boşlukları yazdı
    my_file.seek(0)         #cümle başına götürdü
    print(my_file.read(5))
    print(my_file.read(6))
    print(my_file.tell())  #nerde olduğunu gösterir

#courses=["python", "javascript", "c++", "java", "ruby"] bir dosyaya alt alta yazdır
courses=["python", "javascript", "c++", "java", "ruby"]
with open("courses.txt", "w") as myfile:
    for x in courses:
        myfile.write(f"{x}\n")

#movies.txt her bir sırayı bir listede göster
with open("movies.txt", "r") as my_file:
    file_content= my_file.readlines()
    file_content=[each.strip("\n") for each in file_content if "\n" in each ]
    print(file_content)

#movies.txt dosyasını kopyala
with open("movies.txt", "r") as my_file:
    with open("movies2.txt", "w") as myfile:
        for line in my_file:
            myfile.write(line)
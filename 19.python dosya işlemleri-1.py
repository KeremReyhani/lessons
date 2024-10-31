my_file=open("movies.txt", "r") #r:read
file_content=my_file.read()
print(file_content)

my_file=open("movies.txt", "r")
print(my_file.name)
print(my_file.mode)
print(my_file.read())

my_file.close()
print(my_file.closed)

with open("movies.txt", "r") as myfile:  #bu yapıya context manager denir. dosyaları kapatmamız gerekmez.
    print(myfile.readlines())
    print(myfile.readline())
    print(myfile.readline())

with open("movies.txt", "r") as myfile:
    print(myfile.readline())
    print(myfile.readline())

with open("movies.txt", "r") as myfile:
    for line in myfile:
        print(line)

with open("movies.txt", "r") as myfile:
    print(myfile.read(6)) #karakter sayısı




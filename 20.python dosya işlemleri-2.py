with open("team.txt", "w") as my_file:    #r okuma modu, w yazma modu
    my_file.write("Beşiktaş\n")
    my_file.write("Fenerbahçe\t")
    my_file.write("Galatasaray\n")
    my_file.seek(1)                       #başlangıç noktasını değiştirir
    my_file.write("kerem")
    print("\nTrabzonspor", file=my_file)


with open("team.txt", "a") as my_file: #append mode silmeden yazdırır
    my_file.write("Batman")

with open("data2.txt", "x") as myfile: #create modu
    myfile.write("python\n")
    myfile.write("django\n")
    myfile.write("flask\n")


import csv
with open("22.1.data.csv", "r", encoding="utf-8") as f:
    read_csv=csv.reader(f)
    next(read_csv) #en üst satırı siler.(name, age, gender)
    print(type(read_csv))
    for x in read_csv:
        #        print(x)
        #      print(x[2])
        name=x[0]
        age=x[1]
        gender=x[2]
        print(f"name:{name} | age:{age} | gender: {gender}")



with open("22.1.data.csv", "r", encoding="utf-8") as f, open("22.2.data.csv", "w", encoding="utf-8", newline="") as f2:
    read_csv=csv.reader(f, delimiter=",")
    write_csv=csv.writer(f2, delimiter="-")

    for y in read_csv:
        write_csv.writerow(y)


import sqlite3
#connection=sqlite3.connect("friends.db")
#cursor=connection.cursor()

#with open("friends.txt", "r") as f:
#    for friend in f.readlines():
#        friends=[x.strip() for x in friend.split(",")]
#        cursor.execute("INSERT INTO friends (first_name, last_name, age) VALUES (?,?,?)", (friends[0], friends[1], friends[2]))
#print(friends)

#connection.commit()
#connection.close()



connection=sqlite3.connect("user.db")
cursor=connection.cursor()

#cursor.execute(f"CREATE TABLE users (user TEXT, pass TEXT)")

username=input("Lütfen kullanıcı adınızı giriniz: ")
password=input("Lütfen şifrenizi giriniz: ")

#cursor.execute(f"INSERT INTO users (user, pass) VALUES ('{username}', '{password}')")
cursor.execute(f"SELECT * FROM users WHERE user='{username}' AND pass='{password}'")
if(cursor.fetchone()):
    print("GİRİŞ BAŞARILI")
else:
    print("GİRİŞ BAŞARISIZ")


connection.commit()
connection.close()
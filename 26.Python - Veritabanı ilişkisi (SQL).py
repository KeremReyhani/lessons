#Veri tabanı: Verilerin organize bir şekilde saklandığı yer.
#SQL: Veri tabanı ile iletişimi sağlayan dil.
                                                            #TYPE'LER İÇİN DÖKÜMANTASYON OKUMAYI BİL. (SQLLİTE3 DOCUMENTATİON)
import sqlite3

baglanti=sqlite3.connect("friends.db")
tutucu=baglanti.cursor()
#tutucu.execute("CREATE TABLE friends(first_name TEXT, last_name TEXT, age INTEGER)")
#tutucu.execute("INSERT INTO friends VALUES('Ege', 'Çapo', '19')")
#tutucu.execute("SELECT * FROM friends WHERE first_name='Yusuf'")
#first_name=input("Lütfen adınızı giriniz: ")
#last_name=input("Lütfen soyadınızı giriniz: ")
#age=input("Lütfen yaşınızı giriniz: ")
#1.yol            tutucu.execute(f"INSERT INTO friends VALUES('{first_name}', '{last_name}', {age})")
first_name, last_name, age=input("Lütfen verileri giriniz, Araya virgül koy").split(",")              #üste ayrı yeten girmeye gerek yok
#tutucu.execute("INSERT INTO friends VALUES(?,?,?)", (first_name, last_name, age))       #TUPLE YÖNTEMİ
#tutucu.execute(f"INSERT INTO friends VALUES(:first, :last, :ag)", {'first': first_name, 'last': last_name, 'ag': age})
#tutucu.execute("SELECT * FROM friends WHERE first_name=?", ('Yusuf',))
#tutucu.execute("SELECT * FROM friends")
#tutucu.execute("SELECT * FROM friends ORDER BY first_name DESC")
tutucu.execute("DELETE FROM friends WHERE first_name=?", ("Ege",))
tutucu.execute("UPDATE friends SET last_name=? WHERE last_name=?", ("Reyhani", "Kemahlı"))
print(tutucu.fetchall()) #fetch: verileri getirir.

baglanti.commit()
baglanti.close()
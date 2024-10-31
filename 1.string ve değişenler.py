print("Hello world")
x="besiktas"
print(x)

isim="kerem"
soyisim="reyhani"
print(isim+soyisim)
mesaj="merhaba" + isim
print(mesaj)
mesaj=f"merhaba {soyisim}"
print(mesaj.format(isim))


okul="Yildiz Teknik"
print(len(okul))
print(okul[0])
print(okul[0:8]) #ilk var son yok
print(okul[3:9])
print(okul.title()) #baş harf büyük
print(okul.upper())
print(okul.lower())
print(okul.count("i")) #kaç tane var
print(okul.find("z")) #kaçıncı sırada
print(okul.replace("Teknik", "university"))

print(dir(okul)) #kullanılabilecekler
print(help(str)) #türü yaz



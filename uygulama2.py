#dersler=["matematik", "fizik", "kimya", "ingilizce", "türkçe"] 2. ve son elemanı büyük harfle yaz
dersler=["matematik", "fizik", "kimya", "ingilizce", "türkçe"]
print(dersler[1].upper() + "/" + dersler[4].upper())


#dersler=["matematik", ["fizik", "kimya"], "ingilizce", "türkçe"] fizik ve kimyayı birlikte ve ayrı yaz, son elemanın çıktısını len ile yaz
dersler=["matematik", ["fizik", "kimya"], "ingilizce", "türkçe"]
print(dersler[1])
print(dersler[1][0])
print(dersler[1][1])
print(dersler[len(dersler)-1])


#dersler=["matematik", "fizik", "kimya", "ingilizce", "türkçe"] liste uzunluğunu yaz, tarih dersi ekle, başka yolla coğrafya ekle
dersler=["matematik", "fizik", "kimya", "ingilizce", "türkçe"]
print(len(dersler))
dersler.append("tarih")
print(dersler)
dersler[len(dersler):]=["coğrafya"]
print(dersler)

#numbers=[8,4,5,1,6,9,2,7,3,10] artan ve azalan şekilde sırala
numbers=[8,4,5,1,6,9,2,7,3,10]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

#dersler=[["matematik", "fizik"], ["kimya", "ingilizce"], ["türkçe", "tarih"]] iç listelerin son elemanlarıyla yeni liste oluştur
dersler=[["matematik", "fizik"], ["kimya", "ingilizce"], ["türkçe", "tarih"]]
dersler2=[]
dersler2.append(dersler[0][1] + ", " + dersler[1][1] + ", " + dersler[2][1])
print(dersler2)
                                               #yada
dersler=[["matematik", "fizik"], ["kimya", "ingilizce"], ["türkçe", "tarih"]]
dersler2=[]
for ders in dersler:
    dersler2.append(ders[-1])
print(dersler2)

#1 den 10 a kadar olan sayıların karelerini listele
squares=[]
for number in range(1,11):
    squares.append(number**2)
print(squares)

squares=[num**2 for num in range(1,11)]
print(squares)
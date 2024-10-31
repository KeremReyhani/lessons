import turtle
import random

# Ekran boyutu ve başlık
ekran = turtle.Screen()
ekran.setup(width=600, height=400)
ekran.title("Araba Yarışı")

# Arabaların şekilleri
araba1_sekil = ((-10, 0), (-10, 20), (10, 20), (10, 0))
araba2_sekil = ((-10, 0), (-10, -20), (10, -20), (10, 0))

# Arabaların renkleri
araba1_renk = "red"
araba2_renk = "blue"

# Arabaların başlangıç pozisyonları
araba1_pozisyon = (-250, 100)
araba2_pozisyon = (-250, -100)

# Arabaları oluşturma
araba1 = turtle.Turtle()
araba1.speed(0)
araba1.penup()
araba1.color(araba1_renk)
araba1.shape(araba1_sekil)
araba1.goto(araba1_pozisyon)

araba2 = turtle.Turtle()
araba2.speed(0)
araba2.penup()
araba2.color(araba2_renk)
araba2.shape(araba2_sekil)
araba2.goto(araba2_pozisyon)

# Yarışın bitiş çizgisi
bitis_cizgisi = turtle.Turtle()
bitis_cizgisi.penup()
bitis_cizgisi.goto(250, 200)
bitis_cizgisi.pendown()
bitis_cizgisi.goto(250, -200)

# Yarışın uzunluğu
yaris_uzunlugu = 450

# Arabaların hızları
araba1_hiz = random.randint(1, 5)
araba2_hiz = random.randint(1, 5)

while True:
    araba1.forward(araba1_hiz)
    araba2.forward(araba2_hiz)

    if araba1.xcor() >= yaris_uzunlugu and araba2.xcor() >= yaris_uzunlugu:
        sonuc = "Berabere!"
        break
    elif araba1.xcor() >= yaris_uzunlugu:
        sonuc = "Araba 1 kazandı!"
        break
    elif araba2.xcor() >= yaris_uzunlugu:
        sonuc = "Araba 2 kazandı!"
        break

# Sonuç yazısı
sonuc_yazisi = turtle.Turtle()
sonuc_yazisi.penup()
sonuc_yazisi.goto(0, 0)
sonuc_yazisi.write(sonuc, align="center", font=("Courier", 24, "normal"))

# Pencereyi kapatmak için bekle
turtle.done()

#fonksiyon class içinde kullanılırsa method denir. method'da parantez açılıp kapatılır
class car:
    pass

car_1=car()
car_2=car()

car_1.brand="BMW"
car_1.model="i5"
car_1.year=2010

car_2.brand="AUDI"
car_2.model="x6"
car_2.year=2012
print(car_1)
print(car_1.brand)


class Car:
    def __init__(self, brand, model, year):
        self.brand=brand
        self.model=model
        self.year=year

    def brandmodel(self):
        return f"araba markası {self.brand} ve modeli {self.model}"

Car_1=Car("BMV", "I5", 2010)
Car_2=Car("AUDI", "x6", 2012)
print(Car_1)
print(Car_2.brand)
print(Car_1.brandmodel())


class movie:
    def __init__(self, name, director):
        self.name=name
        self.director=director
movie1=movie("pulp fiction", "tarantino")
movie2=movie("scarface", "de palma")
print(movie1.name)
print(movie2.director)
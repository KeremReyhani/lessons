class Library:
    def __init__(self, amount):
        self.amount=amount

    def method1(self):
        print("Library Method")

class Product:
    def __init__(self, name):
        self.name=name

    def method1(self):
        print("Product Method")

class Series(Library, Product):
    def __init__(self, name, amount, lead_role):
        Product.__init__(self, name)
        Library.__init__(self, amount)
        self.lead_role=lead_role
    def __str__(self):
        return f"Dizi: {self.name} - Miktar: {self.amount} - Başrol: {self.lead_role}"

    def method1(self):
        print("Series Method")

class Movie(Library, Product):
    def __init__(self, name, amount, director):
        Product.__init__(self, name)
        Library.__init__(self, amount)
        self.director=director
    def __str__(self):
        return f"Film: {self.name} - Miktar: {self.amount} - Yönetmen: {self.director}"

#    def method1(self):
#        print("Movie Method")

series1=Series("Sherlock", 4, "Benedict Cumberbatch")
movie1=Movie("Scarface", 1, "Brian De Palma")

print(series1)
#print(help(series1))
print(movie1)
#print(help(movie1))

series1.method1()
movie1.method1() #soldakini yazdırır (POLYMORPHISM denir) - Aynı metodların farklı sonuçlar vermesi

print(isinstance(movie1, Movie)) #1. 2.'nin nesnesiyse True
print(isinstance(movie1, Series))
print(isinstance(movie1, Product))
print(issubclass(Movie, Movie))
print(issubclass(Movie, Series))
print(issubclass(Movie, Library))
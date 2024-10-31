#nesnelere uygulanabilen önceden tanımlı fonksiyonalara dunder fonksiyonlar denir.
class circle:
    pi=3,14
    def __init__(self, radius=1):
        self.radius=radius
    def area(self):
        return self.radius**2*self.pi
    def __repr__(self):
        return f"{__class__.__name__} object with {self.radius} radius"
    def __len__(self):
        return self.radius**2

circle1=circle(5)
print(circle1)
print(circle1.__repr__())

circle2=circle(10)
print(len(circle2))
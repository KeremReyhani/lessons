#inheritance: var olan class'ın metodlarından faydalanarak yeni bir class oluşturmak
class Product:     #Product Book'un parent class'ı
    def __init__(self, name, amount):
        self.__name=name
        self.amount=amount

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name=name


class Book(Product):
    def __init__(self, name, amount, author, publisher):
        super().__init__(name, amount)
        self.author=author
        self.publisher=publisher

    def __str__(self):
        return f"Kitap: {self.get_name()} - Yazar: {self.author} - Yayınevi: {self.publisher} - Miktar: {self.amount}"

books = []


def new_book():
    '''
    Yeni kitap ve kitaba ait bilgileri ekle.
    '''

    namex=input("Yeni kitap ismini giriniz: ")
    authorx=input("Yazar ismini giriniz: ")
    publisherx=input("Yayınevi ismini giriniz: ")
    amount=input("Miktarı giriniz: ")

    book=Book(name=namex, author=authorx, publisher=publisherx, amount=amount)

    books.append(book)

def display_book():
    search_name=input("Kitap ismi giriniz: ")
    book=find_book(search_name)
    if book!=None:
        print(book)
        #print(f"Kitap: {book.name}")
        #print(f"Yazar: {book.author}")
        #print(f"Yayınevi: {book.publisher}")
    else:
        print("Kitap bulunamadı!")

def edit_book():
    """
    İsmi eşleşen kitabı düzenleyeceğiz.
    """
    search_name=input("Kitap ismi giriniz: ")
    book=find_book(search_name)
    if book!=None:
        print("Kitap ismi: ", book.get_name())
        new_name=input("Yeni kitap ismini giriniz, aynı kalması için '.' giriniz: ")
        if new_name!=".":
            book.set_name(new_name)

        new_author =input("Yeni yazar ismini giriniz, aynı kalması için '.' giriniz: ")
        if new_author != ".":
            book.author = new_author

        new_publisher =input("Yeni yayınevi ismini giriniz, aynı kalması için '.' giriniz: ")
        if new_publisher != ".":
            book.publisher= new_publisher
            new_amount = input("Yeni miktarı giriniz, aynı kalması için '.' giriniz: ")
        if new_amount != ".":
            book.amount = new_amount
    else:
        print("Aradığınız kitap bulunamadı!")

def find_book(search_name):
    search_name=search_name.strip()
    search_name=search_name.lower()

    for book in books:
        name=book.get_name()
        name=name.strip()
        name=name.lower()
        if name.startswith(search_name):
            return book
    return None


menu='''Kitap Listesi

1. Kitap Ekle
2. Kitap Bul
3. Kitap Düzenle
4. Çık

Komutunuzu Giriniz: '''

while True:
    command=int(input(menu))
    if command==1:
        new_book()
    elif command==2:
        display_book()
    elif command==3:
        edit_book()
    elif command==4:
        break
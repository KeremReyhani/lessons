#KİTABA AİT BİLGİLERİ DÜZENLE

class Book:
    pass

books = []


def new_book():
    '''
    Yeni kitap ve kitaba ait bilgileri ekle.
    '''
    book=Book()
    book.name=input("Yeni kitap ismini giriniz: ")
    book.author=input("Yazar ismini giriniz: ")
    book.publisher=input("Yayınevi ismini giriniz: ")

    books.append(book)

def display_book():
    search_name=input("Kitap ismi giriniz: ")
    book=find_book(search_name)
    if book!=None:
        print(f"Kitap: {book.name}")
        print(f"Yazar: {book.author}")
        print(f"Yayınevi: {book.publisher}")
    else:
        print("Kitap bulunamadı!")

def edit_book():
    """
    İsmi eşleşen kitabı düzenleyeceğiz.
    """
    search_name=input("Kitap ismi giriniz: ")
    book=find_book(search_name)
    if book!=None:
        print("Kitap ismi: ", book.name)
        new_name=input("Yeni kitap ismini giriniz, aynı kalması için '.' giriniz: ")
        if new_name!=".":
            book.name=new_name

        new_author =input("Yeni yazar ismini giriniz, aynı kalması için '.' giriniz: ")
        if new_author != ".":
            book.author = new_author

        new_publisher =input("Yeni yayınevi ismini giriniz, aynı kalması için '.' giriniz: ")
        if new_publisher != ".":
            book.publisher= new_publisher
    else:
        print("Aradığınız kitap bulunamadı!")

def find_book(search_name):
    search_name=search_name.strip()
    search_name=search_name.lower()

    for book in books:
        name=book.name
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
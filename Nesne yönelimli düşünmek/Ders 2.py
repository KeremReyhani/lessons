class Book: #nesnenin özelliklerini ayrı ayrı barındıracak.
    pass

books = []


def new_book():
    '''
    Yeni kitap ve kitaba ait bilgileri ekle.
    '''
    book=Book()   #book class'ına ait olan nesneyi oluştur ve özellikleri ekle
    book.name=input("Yeni kitap ismini giriniz: ")
    book.author=input("Yazar ismini giriniz: ")
    book.publisher=input("Yayınevi ismini giriniz: ")

    books.append(book)

def find_book():
    search_name=input("Kitap ismi giriniz: ")
    search_name=search_name.strip() #boşlukları siler
    search_name=search_name.lower()
    result= None
    for book in books:
        name=book.name
        name=name.strip()
        name=name.lower()
        if name.startswith(search_name): #ilk kelimeyi girsen de olur.
            result=book
            break
    if result!=0:
        print(f"Kitap: {result.name}")
        print(f"Yazar: {result.author}")
        print(f"Yayınevi: {result.publisher}")
    else:
        print("Aradığınız kitap bulunamadı")

menu='''Kitap Listesi

1. Kitap Ekle
2. Kitap Bul
3. Çık

Komutunuzu Giriniz: '''

while True:
    command=int(input(menu))
    if command==1:
        new_book()
    elif command==2:
        find_book()
    elif command==3:
        break
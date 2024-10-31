#nesne kitaptır. yazar ve yayın evi nesneye ait olan özellikler.
books = []
authors = []
publishers = []

def new_book():
    '''
    Yeni kitap ve yazar bilgisini ekliyoruz.
    '''
    print('Yeni Kitap Ekle')

    books.append(input('Kitap İsmi Giriniz: '))
    authors.append(input('Yazar İsmi Giriniz: '))
    publishers.append(input('Yayınevi İsmi Giriniz: '))


def find_book():
    search_book = input('Kitap İsmi Giriniz: ')
    search_book= search_book.strip()
    search_book = search_book.lower()
    book_position = 0
    for book in books:
        book = book.strip()
        book = book.lower()
        if book.startswith(search_book):
            break
        book_position = book_position + 1

    if book_position < len(books):

        print(f'Kitap:  {books[book_position]}')
        print(f'Yazar:  {authors[book_position]}')
        print(f'Yayınevi:  {publishers[book_position]}')
    else:
        print('Aradığınız Kitap Bulunamadı')

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
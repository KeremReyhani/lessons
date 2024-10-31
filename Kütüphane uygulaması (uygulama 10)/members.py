from book import Book

class Member:
    def __init__(self, name):
        self.name=name
        self.books=[]

    def __repr__(self):
        return f"Member: {self.name}"

    def add_book(self, name, author):
        book=Book(name, author, False)
        self.books.append(book)

    def delete_book(self, name):
        for book in self.books:
            if book.name==name:
                self.books.remove(book)

    def read_book(self):
        read_book_list=[]
        for book in self.books:
            if book.read:
                read_book_list.append(book)
            return read_book_list


    def save_to_file(self):
        with open(f"{self.name}.txt", "w") as f:
            f.write(self.name + "\n")
            for book in self.books:
                f.write(f"{book.name}, {book.author}, {str(book.read)} \n")


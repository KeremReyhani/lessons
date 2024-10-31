from book import Book
from members import Member
book_1=Book("Babalar ve Oğullar", "Turgenyev", True)
book_2=Book("Sherlock Holmes", "Conan Doyle", False)
book_3=Book("Dönüşüm", "Kafka", False)

print(book_1)
print(book_2.name)
print(book_3.author)

member_1=Member("kerem")

print(member_1.read_book())

member_1.books.append(book_1)
member_1.books.append(book_2)
member_1.books.append(book_3)
print(member_1)
print(member_1.books)
print(member_1.read_book())

member_2=Member("Kerem")
member_2.add_book("Hayvan Mezarlığı", "Stephen King")
member_2.add_book("Yabancı", "Albert Camus")
print(member_2.books)

member_2.delete_book("Yabancı")
print(member_2.books)


member_1.save_to_file()

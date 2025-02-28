"""
Author: Macasero, Gabriel S.
Date created: 2/28/2025

https://programming-25.mooc.fi/part-8/3-defining-classes - Defining classes

"""

class Book:
    def __init__(self, name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

def older_book(book1: Book, book2: Book):
    if book1.year > book2.year:
        print(f"{book2.name} is older, it was published in {book2.year}")
    elif book2.year > book1.year:
        print(f"{book1.name} is older, it was published in {book1.year}")
    elif book1.year == book2.year:
        print(f"{book1.name} and {book2.name} were published in {book1.year}")

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

older_book(python, everest)
older_book(python, norma)
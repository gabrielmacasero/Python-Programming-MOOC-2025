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

def books_of_genre(books: list, genre: str):
    if len(books) == 0:
        return []
    else:
        return [book for book in books if book.genre == genre]

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]

print("Books in the crime genre:")
for book in books_of_genre(books, "crime"):
    print(f"{book.author}: {book.name}")
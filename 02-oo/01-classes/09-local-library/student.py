class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.books.append(book)

    def remove_book(self, book):
        for lib_book in self.books:
            if book.title == lib_book.title and book.author == lib_book.author:
                self.books.remove(lib_book)
        for lib_book in self.books:
            if book.title == lib_book.title and book.author == lib_book.author:
                self.books.remove(lib_book)

    def search_books(self, search_string):
        result = []
        for book in self.books:
            if search_string.lower() in book.title.lower():
                result.append(book)
            elif search_string.lower() in book.author.lower():
                result.append(book)

        return result

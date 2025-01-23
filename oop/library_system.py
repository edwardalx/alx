class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
         return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)
    def __str__(self):
         return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
        
class PrintBook(Book):
    def __init__(self, title, author, page_count ):
        super().__init__(title, author)
        self.page_count = int(page_count)
    def __str__(self):
         return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
            self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            print(book)



# library = Library()
# library.add_book(EBook("Digital Fortress", "Dan Brown", 500))
# library.add_book(PrintBook("The Alchemist", "Paulo Coelho", 208))

# print("Library Books:")
# library.list_books()
    
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # def __str__(self):
    #     return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)

    # def __str__(self):
    #     return f"EBook: {self.title} by {self.author}, File size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)

    # def __str__(self):
    #     return f"PrintBook: {self.title} by {self.author}, Page count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []  # A list to store instances of Book, Ebook, and Printbook

    def add_book(self, book):
       # if isinstance(book, Book):  # Ensure only valid Book instances are added
            self.books.append(book)
       # else:
       #     raise ValueError("Only Book instances can be added to the library.")

    def list_books(self):
        #if not self.books:
        #     print("No books in the library.")
        # else:
            for book in self.books:
                print(book)
                '''
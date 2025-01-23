# class Book:
#     def __init__(self, title, author, _is_checked_out = False):
#         self.title = title
#         self.author = author
#         self._is_checked_out =_is_checked_out
#     def check_out(self):
#         if not self._is_checked_out:
#             self._is_checked_out = True
#             return True
#         return False

# class Library():
#     def __init__(self, _books = None):
#         self._books = _books if _books is not None else []

#     def add_book(self,books):
#         self._books.append(books)
#         print(f"Added {self._books}to the library.")
        
#     def check_out_book(self,title):
#         for book in self._books:
#             if book.title in book:
#                 print(title)
#             else: print("book not in List")
        
#     def return_book(self, title):
#         for book in self._books:
#             if title in book:
#                 self._books.remove(title)
#             else: print(f"{title} is not in the list")
#     def list_available_books(self):
#         for book in self._books:
#             print(book)
#         return

class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"You checked out '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' is already checked out.")
                    return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{book.title}' has been returned.")
                    return
                else:
                    print(f"'{book.title}' was not checked out.")
                    return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- '{book.title}' by {book.author}")
        else:
            print("No books available at the moment.")

# For my tests
# mybook1 =Book("Brave New World", "Aldous Huxley") 
# myLib = Library()
# myLib.add_book(mybook1)
# myLib.return_book(mybook1.title)
      
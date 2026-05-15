# Write a Library class with no_of_books and books as two instance variables.
# Write a program to create a library from this Library class and show how you
# can print all books, add a book and get the number of books using different
# methods. Show that your program doesn't persist the books after the program
# is stopped!


class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    # Decorators
    def update_count(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            self.no_of_books = len(self.books)
            return result

        return wrapper

    @update_count
    def add_books(self, book_list):
        self.books.extend(book_list)
        print("Books added successfully.")

    def show_books(self):
        print("\nBooks in Library")
        for book in self.books:
            print("-", book)

    def get_no_of_books(self):
        return self.no_of_books


obj = Library()
# book_list = ["RD Sharma", "MS Chauhan", "Irodov", "Geometry"]
n = int(input("Enter number of books: "))
book_list = []
for i in range(n):
    book = input(f"Enter book {i+1}: ")
    book_list.append(book)

obj.add_books(book_list)
obj.show_books()
print("\nTotal books:", obj.get_no_of_books())

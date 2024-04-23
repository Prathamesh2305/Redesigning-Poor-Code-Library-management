from storage import save_to_file, load_from_file

class Book:
    """A class representing a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN number of the book.
        available (bool): Book availability status, True if the book is available.
    """
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

class BookManager:
    """A class to manage books in the library system."""

    def __init__(self):
        self.books = load_from_file('books.json')

    def add_book(self, title, author, isbn):
        """Add a new book to the library and save it to the storage."""
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        save_to_file(self.books, 'books.json')

    def find_book(self, isbn):
        """Find a book by its ISBN."""
        return next((book for book in self.books if book.isbn == isbn), None)

    def list_books(self):
        """List all books in the library."""
        return self.books

    def check_out_book(self, isbn, user_id):
        """Checks out a book to a user."""
        book = self.find_book(isbn)
        if book and book.available:
            book.available = False
            save_to_file(self.books, 'books.json')
            return f"Book {isbn} checked out by {user_id}"
        return "Book unavailable or not found"

    def check_in_book(self, isbn, user_id):
        """Checks in a book from a user."""
        book = self.find_book(isbn)
        if book and not book.available:
            book.available = True
            save_to_file(self.books, 'books.json')
            return f"Book {isbn} checked in by {user_id}"
        return "Book not checked out or not found"

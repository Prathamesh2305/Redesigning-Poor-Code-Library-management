from models import Book
from storage import save_to_file, load_from_file

books = load_from_file('books.json')

def add_book(title, author, isbn):
    """Add a new book to the library and save it to the storage.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN number of the book.
    """
    new_book = Book(title, author, isbn)
    books.append(new_book)
    save_to_file(books, 'books.json')

def find_book(isbn):
    """Find a book by its ISBN.

    Args:
        isbn (str): The ISBN number of the book to find.

    Returns:
        Book: The book object if found, None otherwise.
    """
    return next((book for book in books if book.isbn == isbn), None)

def list_books():
    """List all books in the library.

    Returns:
        list: A list of all books.
    """
    return books

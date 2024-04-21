from book import books, find_book
from storage import save_to_file

def check_out_book(isbn, user_id):
    """Checks out a book to a user.

    Args:
        isbn (str): The ISBN of the book to check out.
        user_id (str): The ID of the user checking out the book.

    Returns:
        str: Success message if the operation is successful, otherwise an error message.
    """
    book = find_book(isbn)
    if book and book.available:
        book.available = False
        save_to_file(books, 'books.json')
        return f"Book {isbn} checked out by {user_id}"
    return "Book unavailable or not found"

def check_in_book(isbn, user_id):
    """Checks in a book from a user.

    Args:
        isbn (str): The ISBN of the book to check in.
        user_id (str): The ID of the user checking in the book.

    Returns:
        str: Success message if the operation is successful, otherwise an error message.
    """
    book = find_book(isbn)
    if book and not book.available:
        book.available = True
        save_to_file(books, 'books.json')
        return f"Book {isbn} checked in by {user_id}"
    return "Book not checked out or not found"

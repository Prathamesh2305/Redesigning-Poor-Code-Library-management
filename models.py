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

class User:
    """A class representing a user of the library.

    Attributes:
        user_id (str): The unique identifier for the user.
        name (str): The name of the user.
    """
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Book:
    """
    Represents a book in the library system.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN number of the book.
        is_checked_out (bool): Indicates whether the book is currently checked out.
        checked_out_by (str): User ID of the user who has checked out the book, if any.
    """

    def __init__(self, title, author, isbn):
        """
        Initializes a new instance of Book.

        Parameters:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN number of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False
        self.checked_out_by = None

    def __str__(self):
        """
        Returns a string representation of the book, which includes the title,
        author, and ISBN.

        Returns:
            str: A string that represents the book.
        """
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

import logging

logging.basicConfig(filename='library.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class LibraryStorage:
    """
    Manages the storage and operations of books and users in the library system.

    Attributes:
        books (dict): A dictionary of books with ISBN as keys.
        users (dict): A dictionary of users with user IDs as keys.
    """

    def __init__(self):
        """
        Initializes a new instance of LibraryStorage, setting up dictionaries for
        books and users.
        """
        self.books = {}
        self.users = {}


    def add_book(self, book):
        """
        Adds a new book to the library storage.

        Parameters:
            book (Book): The book to be added.

        Returns:
            str: A message indicating the result of the operation.
        """
        if book.isbn in self.books:
            logging.info(f"Attempt to add existing book: {book}")
            return "Book already exists."
        self.books[book.isbn] = book
        logging.info(f"Book added: {book}")
        return "Book added!"


    def update_book(self, isbn, title=None, author=None):
        """
        Updates the details of a book in the library storage.

        Parameters:
            isbn (str): The ISBN of the book to be updated.
            title (str, optional): The new title of the book, if updating.
            author (str, optional): The new author of the book, if updating.

        Returns:
            str: A message indicating the result of the operation.
        """
        if isbn in self.books:
            if title:
                self.books[isbn].title = title
            if author:
                self.books[isbn].author = author
            logging.info(f"Book updated: {self.books[isbn]}")
            return "Update done!"
        else:
            return "Book not found."


    def delete_book(self, isbn):
        """
        Deletes a book from the library storage.

        Parameters:
            isbn (str): The ISBN of the book to be deleted.

        Returns:
            str: A message indicating the result of the operation.
        """
        if isbn in self.books and not self.books[isbn].is_checked_out:
            logging.info(f"Book deleted: {self.books[isbn]}")
            del self.books[isbn]
            return "Book Deleted!"
        else:
            return "Book is currently checked out or not found."


    def list_books(self):
        """
        Lists all books in the library storage.

        Returns:
            list: A list of strings, each representing a book.
        """
        return [f"{str(book)} - {'Available' if not book.is_checked_out else 'Checked out by User ID: ' + book.checked_out_by}" for book in self.books.values()]


    def search_books(self, **kwargs):
        """
        Searches for books based on provided keyword arguments.

        Parameters:
            **kwargs: Variable keyword arguments used for searching books by attributes.

        Returns:
            list: A list of books that match the search criteria.
        """
        results = []
        for book in self.books.values():
            if all(getattr(book, key) == value for key, value in kwargs.items()):
                results.append(book)
        return results


    def add_user(self, user):
        """
        Adds a new user to the library storage.

        Parameters:
            user (User): The user to be added.

        Returns:
            str: A message indicating the result of the operation.
        """
        if user.user_id in self.users:
            logging.info(f"Attempt to add existing user: {user}")
            return "User already exists."
        self.users[user.user_id] = user
        logging.info(f"User added: {user}")
        return "User added!"


    def update_user(self, user_id, name=None):
        """
        Updates the details of a user in the library storage.

        Parameters:
            user_id (str): The user ID of the user to be updated.
            name (str, optional): The new name of the user, if updating.

        Returns:
            str: A message indicating the result of the operation.
        """
        if user_id in self.users:
            if name:
                self.users[user_id].name = name
            logging.info(f"User updated: {self.users[user_id]}")
            return "Update done!"

        else:
            return "User not found."


    def delete_user(self, user_id):
        """
        Deletes a user from the library storage.

        Parameters:
            user_id (str): The user ID of the user to be deleted.

        Returns:
            str: A message indicating the result of the operation.
        """
        if user_id in self.users:
            logging.info(f"User deleted: {self.users[user_id]}")
            del self.users[user_id]
            return "User Deleted!"
        else:
            return "User not found."


    def list_users(self):
        """
        Lists all users in the library storage.

        Returns:
            list: A list of strings, each representing a user.
        """
        return [str(user) for user in self.users.values()]


    def check_out_book(self, isbn, user_id):
        """
        Checks out a book to a user.

        Parameters:
            isbn (str): The ISBN of the book to be checked out.
            user_id (str): The user ID of the user checking out the book.

        Returns:
            str: A message indicating the result of the operation.
        """
        if isbn in self.books and user_id in self.users:
            if not self.books[isbn].is_checked_out:
                self.books[isbn].is_checked_out = True
                self.books[isbn].checked_out_by = user_id  # Track who has checked out the book
                logging.info(f"Book checked out: {self.books[isbn]} by {self.users[user_id]}")
                return f"Book checked out successfully. Book is now checked out by User ID: {user_id}."
            else:
                return f"Book already checked out by User ID: {self.books[isbn].checked_out_by}."
        else:
            return "Book or user not found."


    def check_in_book(self, isbn, user_id):
        """
        Checks in a book that was previously checked out.

        Parameters:
            isbn (str): The ISBN of the book to be checked in.

        Returns:
            str: A message indicating the result of the operation.
        """
        if isbn in self.books:
            if self.books[isbn].is_checked_out and self.books[isbn].checked_out_by == user_id:
                self.books[isbn].is_checked_out = False
                self.books[isbn].checked_out_by = None  # Clear the checkout information
                logging.info(f"Book checked in: {self.books[isbn]}")
                return "Book checked in successfully. Book is now available."
            else:
                return f"Cannot check in. Book was not checked out by this user. Currently checked out by User ID: {self.books[isbn].checked_out_by if self.books[isbn].is_checked_out else 'N/A'}."
        else:
            return "Book not found."


    def book_availability(self, isbn):
        """
        Checks the availability of a specific book.

        Parameters:
            isbn (str): The ISBN of the book to check availability for.

        Returns:
            bool: True if the book is available, False otherwise.
        """
        if isbn in self.books:
            return not self.books[isbn].is_checked_out
        else:
            return False

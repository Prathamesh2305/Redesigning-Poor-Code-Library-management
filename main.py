from storage import LibraryStorage
from book import Book
from user import User

def main():
    """
    The main entry point for the library management system. It initializes the
    library storage and provides a command-line interface for managing the library.

    Uses:
        - Add, update, and delete books and users.
        - Check books in and out.
        - Search and list books and users.
    """
    library = LibraryStorage()

    while True:
        print("\nLibrary Management System")
        print("1. Manage Books")
        print("2. Manage Users")
        print("3. Check Out Book")
        print("4. Check In Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manage_books(library)
        elif choice == '2':
            manage_users(library)
        elif choice == '3':
            check_out_book(library)
        elif choice == '4':
            check_in_book(library)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def manage_books(library):
    print("\nBook Management")
    print("a. Add Book")
    print("b. Update Book")
    print("c. Delete Book")
    print("d. List Books")
    print("e. Search Books")
    choice = input("Enter your choice: ")

    if choice == 'a':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        book = Book(title, author, isbn)
        print(library.add_book(book))
    elif choice == 'b':
        isbn = input("Enter ISBN of the book to update: ")
        title = input("Enter new title (leave blank to not change): ")
        author = input("Enter new author (leave blank to not change): ")
        print(library.update_book(isbn, title=title if title else None, author=author if author else None))
    elif choice == 'c':
        isbn = input("Enter ISBN of the book to delete: ")
        print(library.delete_book(isbn))
    elif choice == 'd':
        print("Listing all books:")
        books = library.list_books()
        for book in books:
            print(book)
    elif choice == 'e':
        search_query = input("Enter search attribute (title/author/isbn): ")
        value = input(f"Enter value for {search_query}: ")
        print("Search results:")
        results = library.search_books(**{search_query: value})
        for result in results:
            print(result)
    else:
        print("Invalid choice.")

def manage_users(library):
    print("\nUser Management")
    print("a. Add User")
    print("b. Update User")
    print("c. Delete User")
    print("d. List Users")
    choice = input("Enter your choice: ")

    if choice == 'a':
        user_id = input("Enter user ID: ")
        name = input("Enter user name: ")
        user = User(user_id, name)
        print(library.add_user(user))
    elif choice == 'b':
        user_id = input("Enter user ID to update: ")
        name = input("Enter new name: ")
        print(library.update_user(user_id, name))
    elif choice == 'c':
        user_id = input("Enter user ID to delete: ")
        print(library.delete_user(user_id))
    elif choice == 'd':
        print("Listing all users:")
        users = library.list_users()
        for user in users:
            print(user)
    else:
        print("Invalid choice.")

def check_out_book(library):
    isbn = input("Enter ISBN of the book to check out: ")
    user_id = input("Enter user ID who is checking out the book: ")
    print(library.check_out_book(isbn, user_id))

def check_in_book(library):
    isbn = input("Enter ISBN of the book to check in: ")
    uid=input("Enter User id who is checking in: ")
    print(library.check_in_book(isbn,uid))

if __name__ == "__main__":
    main()
from book import BookManager
from user import UserManager

def main_menu():
    book_manager = BookManager()
    user_manager = UserManager()

    while True:
        print("\n1. Add Book")
        print("2. List Books")
        print("3. Add User")
        print("4. List Users")
        print("5. Check Out Book")
        print("6. Check In Book")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book_manager.add_book(title, author, isbn)
            print("Book added.")
        elif choice == '2':
            for book in book_manager.list_books():
                print(f"{book.title}, {book.author}, {book.isbn}, {'Available' if book.available else 'Checked out'}")
        elif choice == '3':
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            user_manager.add_user(user_id, name)
            print("User added.")
        elif choice == '4':
            for user in user_manager.list_users():
                print(f"{user.user_id}: {user.name}")
        elif choice == '5':
            isbn = input("Enter book ISBN to check out: ")
            user_id = input("Enter user ID: ")
            result = book_manager.check_out_book(isbn, user_id)
            print(result)
        elif choice == '6':
            isbn = input("Enter book ISBN to check in: ")
            user_id = input("Enter user ID: ")
            result = book_manager.check_in_book(isbn, user_id)
            print(result)
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()

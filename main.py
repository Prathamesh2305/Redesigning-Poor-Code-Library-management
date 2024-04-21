from book import add_book, list_books
from user import add_user, list_users
from check import check_out_book, check_in_book

def main_menu():
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
            add_book(title, author, isbn)
            print("Book added.")
        elif choice == '2':
            for book in list_books():
                print(f"{book.title}, {book.author}, {book.isbn}, {'Available' if book.available else 'Checked out'}")
        elif choice == '3':
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            add_user(user_id, name)
            print("User added.")
        elif choice == '4':
            for user in list_users():
                print(f"{user.user_id}: {user.name}")
        elif choice == '5':
            isbn = input("Enter book ISBN to check out: ")
            user_id = input("Enter user ID: ")
            result = check_out_book(isbn, user_id)
            print(result)
        elif choice == '6':
            isbn = input("Enter book ISBN to check in: ")
            user_id = input("Enter user ID: ")
            result = check_in_book(isbn, user_id)
            print(result)
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()

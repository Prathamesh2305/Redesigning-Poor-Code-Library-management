from storage import save_to_file, load_from_file

class User:
    """A class representing a user of the library.

    Attributes:
        user_id (str): The unique identifier for the user.
        name (str): The name of the user.
    """
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class UserManager:
    """A class to manage users in the library system."""

    def __init__(self):
        self.users = load_from_file('users.json')

    def add_user(self, user_id, name):
        """Add a new user to the library system."""
        new_user = User(user_id, name)
        self.users.append(new_user)
        save_to_file(self.users, 'users.json')

    def find_user(self, user_id):
        """Find a user by their user ID."""
        return next((user for user in self.users if user.user_id == user_id), None)

    def list_users(self):
        """List all users in the library system."""
        return self.users

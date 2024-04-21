from models import User
from storage import save_to_file, load_from_file

users = load_from_file('users.json')

def add_user(user_id, name):
    """Add a new user to the library system.

    Args:
        user_id (str): The unique identifier for the user.
        name (str): The name of the user.

    Creates a new user object and appends it to the list of users. The list is then
    saved to the JSON file to update the persistent storage.
    """
    new_user = User(user_id, name)
    users.append(new_user)
    save_to_file(users, 'users.json')

def find_user(user_id):
    """Find a user by their user ID.

    Args:
        user_id (str): The unique identifier for the user to find.

    Returns:
        User: The user object if found, None otherwise.

    This function searches through the list of users and returns the user object
    if the ID matches. If no user is found with the given ID, it returns None.
    """
    return next((user for user in users if user.user_id == user_id), None)

def list_users():
    """List all users in the library system.

    Returns:
        list: A list of all user objects.

    This function returns a list of all user objects currently stored in the system.
    Each user object includes the user's ID and name.
    """
    return users

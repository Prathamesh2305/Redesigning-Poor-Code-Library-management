import json

def save_to_file(data, filename):
    """Save a list of objects to a JSON file."""
    with open(filename, 'w') as file:
        json.dump([obj.__dict__ for obj in data], file)

def load_from_file(filename):
    """Load data from a JSON file and convert it into a list of objects."""
    from book import Book
    from user import User  # Importing locally to avoid circular dependency

    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            if filename == 'books.json':
                return [Book(**item) for item in data]
            elif filename == 'users.json':
                return [User(**item) for item in data]
    except FileNotFoundError:
        return []

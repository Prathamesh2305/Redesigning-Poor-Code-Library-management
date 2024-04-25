class User:
    """
    Represents a user in the library system.

    Attributes:
        user_id (str): The unique identifier for the user.
        name (str): The name of the user.
    """

    def __init__(self, user_id, name):
        """
        Initializes a new instance of User.

        Parameters:
            user_id (str): The unique identifier for the user.
            name (str): The name of the user.
        """
        self.user_id = user_id
        self.name = name

    def __str__(self):
        """
        Returns a string representation of the user, which includes the user ID
        and the name.

        Returns:
            str: A string that represents the user.
        """
        return f"User ID: {self.user_id}, Name: {self.name}"

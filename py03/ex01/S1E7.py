from S1E9 import Character


class Baratheon(Character):
    """I am a Baratheon"""
    def __init__(self, first_name: str, is_alive=True) -> None:
        """
        This constructor is used to instanciate a Baratheon character.

        Parameters:
        -`first_name` (str): The first name of the character as a string
        - `is_alive` (bool, optional): a bool var set to True by default
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """
        `die` method sets the `is_alive` variable to false.
        """        
        self.is_alive = False


class Lannister(Character):
    """I am a Lannister"""
    def __init__(self, first_name: str, is_alive=True) -> None:
        """
        This constructor is used to instanciate a Lannister character.

        Parameters:
        -`first_name` (str): The first name of the character as a string
        - `is_alive` (bool, optional): a bool var set to True by default
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """
        `die` method sets the `is_alive` variable to false.
        """
        self.is_alive = False

    # decorator
    def create_lannister() -> :
        new_character = 
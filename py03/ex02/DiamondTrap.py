from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """I am the King of Westeros"""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Class Constructor
        Parameters:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive.
            Defaults to True."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        """eye setter method"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """hairs setter method"""
        self.hairs = hairs

    def get_eyes(self):
        """eye getter method"""
        return self.eyes

    def get_hairs(self):
        """hairs getter method"""
        return self.hairs

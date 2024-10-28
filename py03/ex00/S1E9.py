from abc import ABC, abstractmethod


class Character(ABC):
    """I am an Abstract Character
    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): Indicates whether the character is alive.
        Defaults to True."""

    def __init__(self, first_name: str, is_alive=True) -> None:
        """Class Constructor
        Parameters:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive.
            Defaults to True."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Method to change the character's state to dead by setting is_alive
        to False."""
        self.is_alive = False


class Stark(Character):
    """Representing the Stark family"""

    def die(self) -> None:
        """`die` method sets the `is_alive` variable to false."""
        super().die()

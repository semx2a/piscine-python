from abc import ABC, abstractmethod


class Character(ABC):
    """I am an Abstract Character
    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): Indicates whether the character is alive.
        Defaults to True."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive=True) -> None:
        """Class Constructor
        Parameters:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive.
            Defaults to True."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """Method to change the character's state to dead by setting is_alive
to False."""
        self.is_alive = False


class Stark(Character):
    """Representing the Stark family"""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Class Constructor
        Parameters:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive.
            Defaults to True."""

        super().__init__(first_name, is_alive)

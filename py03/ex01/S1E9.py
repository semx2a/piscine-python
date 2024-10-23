from abc import ABC, abstractmethod


class Character(ABC):
    """I am an Abstract Character"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive=True) -> None:
        pass

    @abstractmethod
    def die(self) -> None:
        pass


class Stark(Character):
    """
    I am a Stark
    """
    def __init__(self, first_name: str, is_alive=True) -> None:
        """
        This constructor is used to instanciate a Stark character.

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

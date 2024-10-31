from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family
    Attributes:
        family_name (str): The family name, "Baratheon".
        eyes (str): The eye color of the family.
        hairs (str): The hair color of the family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Class Constructor
        Parameters:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive.
            Defaults to True."""

        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'


class Lannister(Character):
    """Representing the Lannister family
    Attributes:
        family_name (str): The family name, "Baratheon".
        eyes (str): The eye color of the family.
        hairs (str): The hair color of the family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Class Constructor
        Parameters:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive.
            Defaults to True."""

        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)

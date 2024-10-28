from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family
    Attributes:
        family_name (str): The family name, "Baratheon".
        eyes (str): The eye color of the family.
        hairs (str): The hair color of the family."""
    family_name = 'Baratheon'
    eyes = 'brown'
    hairs = 'dark'

    def __str__(self):
        """Returns a string representation of the Baratheon character."""
        return f"Vecor :('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns a string representation for debugging"""
        return self.__str__()

    def die(self):
        super().die()


class Lannister(Character):
    """Representing the Lannister family
    Attributes:
        family_name (str): The family name, "Baratheon".
        eyes (str): The eye color of the family.
        hairs (str): The hair color of the family."""
    family_name = 'Lannister'
    eyes = 'blue'
    hairs = 'light'

    def __str__(self):
        """Returns a string representation for debugging"""
        return f"Vecor :('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns a string representation of the Lannister character."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)

    def die(self):
        super().die()

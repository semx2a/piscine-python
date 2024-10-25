from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    family_name = 'Baratheon'
    eyes = 'brown'
    hairs = 'dark'


class Lannister(Character):
    """Representing the Lannister family"""
    family_name = 'Lannister'
    eyes = 'blue'
    hairs = 'light'

    # provides the official string representation of an object, 
    # aimed at the programmer.
    def __repr__(self):  # 'dunder method'
        pass
    
    # provides the informal string representation of an object, 
    # aimed a the user.
    def __str__(self):  
        pass
    
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
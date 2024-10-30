import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass(repr=True)
class Student:
    """
    Dataclass representing information about a student.

    Args:
    - name: first name of the student
    - surname: last name of the student

    Class variables that cannot be initialized.
    - active: wether the student is still active or not. Set to True by default
    - login: concatenation of first letter of capitalized name and
    surname in lowercase
    - id: randomly generated id
    """

    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = self.name[0].capitalize() + self.surname.lower()

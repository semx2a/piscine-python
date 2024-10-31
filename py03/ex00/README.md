# Exercise 00: GOT S1E9

## Description

You must provide the following elements in your code:

- An **abstract** class `character` which can takes the following parameters:
  - `first_name`
  - `is_alive : Bool` (default is True, optional argument)
  - a method `die` which sets `is_alive` to False
- A class `Stark` which inherits from `character`

Each method must have a docstring.

## Design choices

I chose to make the `__init__` method of the `Character` class abstract.
The rationale behind this decision is this method is the one most prone to change, and it is the one that is most likely to be overridden by a subclass.

## References

- [Abstract class](https://www.pythoncheatsheet.org/cheatsheet/oop-basics#abstraction)
- [Python OOP Basics](https://www.pythoncheatsheet.org/cheatsheet/oop-basics)
- [Python functions optional arguments](https://realpython.com/python-optional-arguments/)
- [Python super](https://realpython.com/python-super/)

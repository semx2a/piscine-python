# Exercise 00: Hello, World!

## Instructions

You need to modify the string of each data object to display the following greetings:
"Hello World", "Hello «country of your campus»", "Hello «city of your campus»", "Hello
«name of your campus»"

```py
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
```

Expected output:

```sh
$>python Hello.py | cat -e
['Hello', 'World!']$
('Hello', 'France!')$
{'Hello', 'Paris!'}$
{'Hello': '42Paris!'}$
$>
```

## Data Types

To solve this exercise, I researched the different data types in Python using the hints in the exercise's subject.

I found out there are four collection built-in data types in Python:

- `List` is a collection which is ordered and changeable. Allows duplicate members.
- `Tuple` is a collection which is ordered and unchangeable. Allows duplicate members.
- `Set` is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
- `Dictionary` is a collection which is ordered** and changeable. No duplicate members.

I quickly was able to find the syntax for each data type and how to modify the data in each type.

## Usage

This program requires Python 3.10

```sh
python3.10 Hello.py | cat -e
```

## References

- [Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [Python Tuples](https://www.w3schools.com/python/python_tuples.asp)
- [Python Sets](https://www.w3schools.com/python/python_sets.asp)
- [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
- [Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)

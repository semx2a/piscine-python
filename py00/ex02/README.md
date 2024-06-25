# Exercise 2: First function in Python

## Instructions

Write a function that prints the object types and returns 42.

Here’s how it should be prototyped:

```python
def all_thing_is_obj(object: any) -> int:
#your code here
```

Your tester.py:

```python
from find_ft_type import all_thing_is_obj
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
```

Expected output:

```sh
$>python tester.py | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
```

## Usage

```sh
$>python tester.py | cat -e
```

## References

- [Python Functions - Programmiz](https://www.programiz.com/python-programming/function)
- [Python type() - Programiz](https://www.programiz.com/python-programming/methods/built-in/type)
- [Switch case in Python - FreeCodeCamp](https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/)

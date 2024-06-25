# Exercise 00 - Give my BMI

## Description

| Program name | give_my_bmi |
| ------------ | ----------- |
| Turn in files | give_my_bmi.py |
| Allowed functions | numpy or any lib of table manipulation |

## Objective

The `give_bmi` function takes 2 lists of integers or floats as parameters and returns a list of BMI values.
The `apply_limit` function takes a list of integers or floats and an integer representing a limit as parameters. It returns a list of booleans (True if above the limit).
You have to handle error cases if the lists are not the same size, are not int or float.

Below are the function prototypes:

```python
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
#your code here
def apply_limit(bmi:list[int | float], limit: int) -> list[bool]:
#your code here
```

A tester is provided:

```python
from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
```

The output should be:

```python
$> python tester.py
[22.507863455018317, 29.0359168241966] <class 'list'>
[False, True]
```

## Resources
- [Create Your Own ufunc](https://www.w3schools.com/python/numpy/numpy_ufunc_create_function.asp)

# Exercise 01: 2D Array

## Description

| Program name | array2D |
| ------------ | ----------- |
| Turn in files | array2D.py |
| Allowed functions | numpy or any lib of table manipulation |

## Instructions

Write a function that takes a 2D array and a start and end arguments. It prints the array's shape, and returns a truncated version of the array based on the start and end arguments.

The function's prototype is as follows:

```python
def slice_me(family: list, start: int, end: int) -> list:
    # your code here
```

A tester is provided:

```python
from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
```

The output should be:

```bash
$> python tester.py
My shape is: (4, 2)
My new shape is: (2, 2)
[[1.8, 78.4], [2.15, 102.7]]
My shape is: (4, 2)
My new shape is: (1, 2)
[[2.15, 102.7]]
```

## Resources

- [Numpy Array Shape](https://www.w3schools.com/python/numpy/numpy_array_shape.asp)
# Exercise 6: Remake Filter

## Instructions

Allowed functions: sys or any other library that allows you to receive args

**Part 1:**
Recode your own ft_filter, it should behave like the original built-in function (it should return the same thing as `print(filter.__doc__)`, you should use list comprehensions to recode your ft_filter.

>Of course using the original filter built-in is forbidden

**Part 2: The program**
Create a program that accepts two arguments: a string(S), and an integer(N). The program should output a list of words from S that have a length greater than N.

- Words are separated from each other by space characters.
- Strings do not contain any special characters. (Punctuation or invisible)
- The program must contain at least one list comprehension expression and one lambda.
- If the number of argument is different from 2, or if the type of any argument is wrong, the program prints an AssertionError

**Expected outputs:**

```bash
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$>
```

```bash
$> python filterstring.py 'Hello the World' 99
[]
$>
```

```bash
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>
```

```bash
$> python filterstring.py
AssertionError: the arguments are bad
$>
```

## References

- [Python List Comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)
- [Python Filter() function](https://www.w3schools.com/python/ref_func_filter.asp)
- [Python Lambda](https://www.w3schools.com/python/python_lambda.asp)
- [How to use Python Lambda Functions](https://realpython.com/python-lambda)
- [Rationale of Python yield](https://www.reddit.com/r/learnpython/comments/rzukrb/what_is_the_idea_of_using_yield_in_python/)
- [La fonction yield](https://developpement-informatique.com/article/149/la-fonction-yield)

# Exercise 5: First standalone program in Python

## Instructions

**Allowed functions :** sys or any other library that allows to receive the args

This time you have to make a real autonomous program, with a main, which takes
a single string argument and displays the sums of its upper-case characters, lower-case characters, punctuation characters, digits and spaces.

- If None or nothing is provided, the user is prompted to provide a string.
- If more than one argument is provided to the program, print an AssertionError.
Expected outputs:

```sh
$>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backwardcompatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
8 punctuation marks
25 spaces
15 digits
$>
```

Expected outputs: (the carriage return counts as a space, if you don’t want to return one use ctrl + D)

```sh
$>python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
$>
```

## References

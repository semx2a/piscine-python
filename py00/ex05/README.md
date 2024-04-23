# Exercise 5: First standalone program in Python

## Instructions

**Allowed functions :** sys or any other library that allows to receive the args

This time you have to make a real autonomous program, with a main, which takes a single string argument and displays the sums of its upper-case characters, lower-case characters, punctuation characters, digits and spaces.

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

- [Python - Common String Operations - String Constants](https://docs.python.org/3/library/string.html)
- [Python RegEx](https://www.w3schools.com/python/python_regex.asp)
- [5 Best Ways to Count Numbers in Python String](https://blog.finxter.com/5-best-ways-to-count-the-number-of-spaces-in-a-python-string/#:~:text=The%20count()%20method%20in,count()%20on%20the%20string.)
- [Python - Catching multiple excpetions](https://rollbar.com/blog/python-catching-multiple-exceptions/)
- [Python Catching EOFError](https://stackoverflow.com/questions/74283683/eof-error-occurs-when-trying-to-give-a-user-input)
- [Python - How to return multiple values](https://note.nkmk.me/en/python-function-return-multiple-values/)
- [Unpack Tupe and List in Python](https://note.nkmk.me/en/python-tuple-list-unpack/)

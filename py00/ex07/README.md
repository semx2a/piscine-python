# Exercise 7: Dictionnaries SoS

## Instructions

| Files to turn in | sos.py |
|-------------------|--------|
| Allowed libraries | sys or any other library that allows to receive args |

Make a program that takes a string as an argument and encodes it into Morse Code.
• The program supports space and alphanumeric characters
• An alphanumeric character is represented by dots '.' and dashes '-'
• Complete morse characters are separated by a single space
• A space character is represented by a slash '/'

You must use a dictionary to store your morse code.

```python
NESTED_MORSE = { " ": "/ ",
"A": ".- ",
...
```

If the number of arguments is different from 1, or if the type of any argument is wrong, the program prints an AssertionError.

```sh
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
```

## References

- [International Morse Code](https://en.wikipedia.org/wiki/Morse_code)
- [Python all()](https://www.programiz.com/python-programming/methods/built-in/all)
- [Python String upper](https://www.programiz.com/python-programming/methods/string/upper)

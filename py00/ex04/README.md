# Exercise 4: The Even and the Odd

## Instructions

Allowed functions : sys or any other library that allows to receive the args

Create a script that takes a number as argument, checks whether it is odd or even,
and prints the result.
If more than one argument is provided or if the argument is not an integer, print an
AssertionError.

Expected output:
```sh
$> python whatis.py 14
I'm Even.
$>
$> python whatis.py -5
I'm Odd.
$>
$> python whatis.py
$>
$> python whatis.py 0
I'm Even.
$>
$> python whatis.py Hi!
AssertionError: argument is not an integer
$>
$> python whatis.py 13 5
AssertionError: more than one argument provided
```

## Usage

```sh
$> python whatis.py 14
```

or

```sh
$> chmod +x tester.sh && ./tester.sh
```

## References

- [Python Main Function - DigitalOcean](https://www.digitalocean.com/community/tutorials/python-main-function)
- [The Ultimate Guide to Command Line Arguments in Python Scripts](https://moez-62905.medium.com/the-ultimate-guide-to-command-line-arguments-in-python-scripts-61c49c90e0b3#:~:text=In%20Python%2C%20command%2Dline%20arguments,arguments%20passed%20to%20the%20script.)
- [python command line arguments in main, skip script name](https://stackoverflow.com/questions/19016702/python-command-line-arguments-in-main-skip-script-name)
- [Python indexing and slicing](https://realpython.com/lessons/indexing-and-slicing/)
- [Python Lambda](https://www.w3schools.com/python/python_lambda.asp)
- [Python | Assertion Error](https://www.geeksforgeeks.org/python-assertion-error/)
- [How to handle AssertionError in Python and find out which line or statement it occurred on?](https://stackoverflow.com/questions/11587223/how-to-handle-assertionerror-in-python-and-find-out-which-line-or-statement-it-o)
- [Python casting](https://www.w3schools.com/python/python_casting.asp)

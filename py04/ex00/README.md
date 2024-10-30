# Exercise 01: Statistics

## Description

You must take a list of integers and compute the `Mean`, `Median`, `Quartile` (25% and 75%), `Standard Deviation` and `Variance` according to the **kwargs values.
Error handling is required for the following cases:

- If the list is empty, print "ERROR" and return `None`.

Requiered Tests:

```python
from statistics import ft_statistics
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
```

Expected output:

```bash
$> python tester.py
mean : 95.6
median : 42
quartile : [11.0, 64.0]
-----
std : 17982.70124086944
var : 323377543.9183673
-----
-----
ERROR
ERROR
ERROR
```

## Design and Implementation

### A word about error handling

I chose to print "ERROR" and return `None` because the subject's expected output shows that the last call to ft_statistics (i.e. the one with no arguments) should print "ERROR" three times.

I guessed that the reason why the standard output printed 'ERROR' three times was because the function called each function linked to each arguments (i.e. mean, median and quartile).

I couldn't use a simple try/except block because the function would stop at the first error and not print the other errors, when I needed the program to keep running and print all the errors.

Therefore, I chose to add a condition to check if the list is empty and print "ERROR" and return `None` if it is at the start of every function linked to the arguments.

This solution is not one I would've chosen for this exercise and I am unsure of its usefulness in a real-world scenario. I would've preferred to raise an exception and catch it in the main function, but I wanted to stick to the expected output.

## Resources

- [Args and Kwargs in Python](https://www.pythoncheatsheet.org/blog/python-easy-args-kwargs)
- [Mean formula](https://www.cuemath.com/data/mean/)
- [Median formula](https://www.cuemath.com/data/median/)
- [Quartile Formula](https://www.cuemath.com/quartile-formula/)
- [Standard Deviation Formula](https://discovery.cs.illinois.edu/guides/Statistics-with-Python/calculating-std-in-python/)
- [Variance Formula](https://stackabuse.com/calculating-variance-and-standard-deviation-in-python/)

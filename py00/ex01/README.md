# Exercise 01: Introduction to packages

## Instructions

Write a script that formats the dates this way, of course your date will not be mine
as in the example but it must be formatted the same.
Expected output:

```sh
$>python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
```

## Libraries

The script will use the `datetime` library to format the date. The `datetime` library is a built-in Python library that allows you to work with dates and times.

## Usage

This program requires Python 3.10

```sh
python3.10 format_ft_time.py | cat -e
```

## References

- [Python Datetimes](https://docs.python.org/3/library/datetime.html#timedelta-objects)
- [strftime method from datetime lib](https://www.w3schools.com/python/python_datetime.asp): to format the date
- [Python Scientific Notation](https://www.w3schools.com/python/ref_func_format.asp): to format the scientific notation
- [Python Scientific Notation Explained](https://www.scaler.com/topics/python-scientific-notation/)
- [f-strings](https://he-arc.github.io/livre-python/fstrings/index.html): to format the date
- [Day of the month as decimal number](https://www.programiz.com/python-programming/datetime/strftime#:~:text=Day%20of%20the%20month%20as%20a%20decimal%20number.): to format the date

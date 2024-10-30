# Exercise 02: Call Limit

## Description

Write a function that takes as argument a call limit of another function and blocks its execution above a limit.

Expected output:

```bash
$> python tester.py
f()
g()
f()
Error: <function g at 0x7fabdc243ee0> call too many times
f()
Error: <function g at 0x7fabdc243ee0> call too many times
$>
```

## References

- [python wrapper function taking arguments inside decorator](https://stackoverflow.com/questions/30904486/python-wrapper-function-taking-arguments-inside-decorator)
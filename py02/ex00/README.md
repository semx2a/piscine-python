# Exercise 00: Load my Dataset

## Description

| Program name | `load` |
| ------------ | --------------- |
| File to turn in | `load_csv.py` |
| Allowed functions | pandas or any lib for dataset manipulation |

## load()

The `load()` loads a csv file, prints its dimensions, and returns the dataset.

### load() Syntax

```python
def load(path:str) -> Dataset:
    pass
```

### load() Parameters

The `load()` function takes a single parameter path, which is a string containing the path of the file.

### load() Return Value

`load()` function returns a dataset if the file is loaded successfully. Otherwise, it returns None.

## References

- [Pandas](https://pandas.pydata.org/)
- [Dataset](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
- [Pandas CSV reader](https://www.w3schools.com/python/pandas/pandas_csv.asp)
- [Pandas DataFrame shape](https://stackoverflow.com/questions/13921647/python-dimension-of-data-frame)
- [Pandas Exceptions](https://stackoverflow.com/questions/64302419/what-are-all-of-the-exceptions-that-pandas-read-csv-throw)

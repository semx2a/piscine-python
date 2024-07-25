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
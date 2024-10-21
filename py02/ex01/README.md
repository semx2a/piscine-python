# Exercise 1: Draw my country

## Description

| Program name | `life_expectancy` |
| ------------ | --------------- |
| File to turn in | `load_csv.py` `aff_life.py` |
| Allowed functions | matplotlib, seaborn or any lib for Data Visualization |

## life_expectancy()

The `life_expectancy()` function calls the load function from the previous exercise, loads the life_expectancy.csv file, and displays the life expectancy of the selected country.

### life_expectancy() Syntax

```python
def life_expectancy(country:str) -> None:
    pass
```

### life_expectancy() Parameters

The `life_expectancy()` function takes a single parameter country, which is a string containing the name of the country.

### life_expectancy() Return Value

`life_expectancy()` function does not return anything.

## notes about the loaded data

The exercise explicitely states that the loaded file should be the `life_expectancy_years.cvs`.
For this reason, any other file will be considered invalid, resulting in the function's behavior being undefined.

## References

- [Pandas: Indexing and Selecting Data](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [Pandas: Dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- [Numpy: Flatten](https://numpy.org/doc/2.0/reference/generated/numpy.ndarray.flatten.html)
- [Seaborn Lineplot](https://seaborn.pydata.org/generated/seaborn.lineplot.html)
- [How to convert Pandas DataFrame to list](https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-a-list/)
- [How to get column names in Pandas](https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/)
- [An introduction to seaborn](https://seaborn.pydata.org/tutorial/introduction.html)
- [How to search Pandas DataFrame by Index or Value](https://saturncloud.io/blog/how-to-search-pandas-data-frame-by-index-value-and-value-in-any-column/)
- [Creating your first chart using seaborn](https://frankcorso.dev/seaborn.html)
- [Adjust number of ticks in Seaborn plots](https://www.geeksforgeeks.org/how-to-adjust-number-of-ticks-in-seaborn-plots/)
- [Pandas dtype](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html)

# Exercise 1: Draw my year

## Description

| Program name | `gdp_life_expectancy` |
| ------------ | --------------- |
| File to turn in | `load_csv.py` `projection_life.py` |
| Allowed functions | matplotlib, seaborn or any lib for Data Visualization |

## gdp_life_expectancy()

The `gdp_life_expectancy()` function calls the load function , loads the `income_per_person_gdppercapita_ppp_inflation_adjusted.csv` and `life_expectancy_years.csv` files, and displays the projection of life expectancy in relation to the gross national product of the year 1900 for all countries.

### gdp_life_expectancy() Syntax

```python
def gdp_life_expectancy(year: str) -> None:
    pass
```

### gdp_life_expectancy() Parameters

The `gdp_life_expectancy()` function takes a parameter year that is a string containing the year to plot.

### gdp_life_expectancy() Return Value

`gdp_life_expectancy()` function does not return anything.

## notes about the loaded data

The exercise explicitely states that the loaded files should be `income_per_person_gdppercapita_ppp_inflation_adjusted.csv` and `life_expectancy_years.csv`.
For this reason, any other file will be considered invalid, resulting in the function's behavior being undefined.

## References

- [Compare two DataFrames with different size](https://stackoverflow.com/questions/44414876/compare-two-pandas-dataframe-with-different-size)
- [Pandas merge](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)
- [Get list of pandas dataframe columns based on data types](https://stackoverflow.com/questions/22470690/get-list-of-pandas-dataframe-columns-based-on-data-type)
- [Pandas scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html)

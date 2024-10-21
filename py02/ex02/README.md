# Exercise 1: Compare my country

## Description

| Program name | `population_total` |
| ------------ | --------------- |
| File to turn in | `load_csv.py` `aff_pop.py` |
| Allowed functions | matplotlib, seaborn or any lib for Data Visualization |

## population_total()

The `population_total()` function calls the load function , loads the population_total.csv file, and displays the population evolution of the selected countries.
The years to be displayed range from 1800 to 2050.

### population_total() Syntax

```python
def population_total(test_country:str, compare_country: str) -> None:
    pass
```

### population_total() Parameters

The `population_total()` function takes two parameters: tested_country and compared_country, which are both a string containing the name of a country, both different.

### population_total() Return Value

`population_total()` function does not return anything.

## notes about the loaded data

The exercise explicitely states that the loaded file should be the `population_total.cvs`.
For this reason, any other file will be considered invalid, resulting in the function's behavior being undefined.

## References
- [How to convert number abbreviations](https://stackoverflow.com/questions/63722278/how-to-convert-number-abbreviation-1-70-m-1-600-b-2-1m-into-integers-in-py)
- [How to create a multiline plot using seaborn](https://stackoverflow.com/questions/52308749/how-do-i-create-a-multiline-plot-using-seaborn)
-
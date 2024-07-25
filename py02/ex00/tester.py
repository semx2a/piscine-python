from load_csv import load

print(load('../data/life_expectancy_years.csv'))
print(load('../data/wrong_data/empty.csv'))
print(load('../data/wrong_data/invalid_data.csv'))
print(load('../data/wrong_data/char.csv'))
print(load('../data/wrong_data/income_per_gdpcapita_ppp_inflation_adjusted.xlsx'))
print(load('../../py01/assets/animal.jpeg'))

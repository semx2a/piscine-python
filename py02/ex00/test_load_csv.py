import pytest
import os
from load_csv import load


# Determine the absolute path to the assets directory
current_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(current_dir, '../data/')


@pytest.mark.parametrize('path', [
    os.path.join(assets_dir,
                 'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'),
    os.path.join(assets_dir, 'life_expectancy_years.csv'),
    os.path.join(assets_dir, 'population_total.csv')
])
def test_load_runs_without_erros(path):
    load(path)


@pytest.mark.parametrize('path', [
    os.path.join(assets_dir,
                 'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'),
    os.path.join(assets_dir, 'life_expectancy_years.csv'),
    os.path.join(assets_dir, 'population_total.csv')
])
def test_load_runs_with_errors(path):
    load(path)

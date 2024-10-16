import pytest
import os
import pandas as pd
from load_csv import load


# Determine the absolute path to the assets directory
current_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(current_dir, '../data/')
wrong_data = os.path.join(assets_dir, 'wrong_data/')


@pytest.mark.parametrize('path', [
    os.path.join(assets_dir,
                 'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'),
    os.path.join(assets_dir, 'life_expectancy_years.csv'),
    os.path.join(assets_dir, 'population_total.csv')
])
def test_load_runs_without_errors(path):
    df = load(path)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty


@pytest.mark.parametrize('path', [
    os.path.join(wrong_data,
                 'income_per_gdpcapita_ppp_inflation_adjusted.xlsx'),
    os.path.join(wrong_data, 'invalid_data.csv'),
    os.path.join(wrong_data, 'char.csv'),
    os.path.join(wrong_data, 'empty.csv'),
    'README.md',
    '',
    ' '
])
def test_load_runs_with_errors(path):
    with pytest.raises((SystemExit,
                        pd.errors.EmptyDataError,
                        pd.errors.ParserError)):
        load(path)

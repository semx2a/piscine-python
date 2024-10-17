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
                 'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'),
])
def test_load_invalid_data(path):
    with pytest.raises(pd.errors.ParserError):
        assert load(path) is None


@pytest.mark.parametrize('path', [
    os.path.join(wrong_data, 'empty.csv'),
    os.path.join(wrong_data, 'invalid_data.csv'),
    os.path.join(wrong_data, 'char.csv'),
])
def test_load_empty_data(path):
    with pytest.raises(pd.errors.EmptyDataError):
        assert load(path) is None


@pytest.mark.parametrize('path', [
    os.path.join(current_dir, 'README.md'),
    os.path.join(wrong_data,
                 'income_per_person_gdppercapita_ppp_inflation_adjusted.xlsx')

])
def test_load_wrong_filetype(path):
    with pytest.raises(ValueError):
        assert load(path) is None


@pytest.mark.parametrize('path', [
    os.path.join(current_dir, 'doesntexist.txt'),
])
def test_load_file_not_found(path):
    with pytest.raises(FileNotFoundError):
        assert load(path) is None

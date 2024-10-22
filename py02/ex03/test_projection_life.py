import pytest
from projection_life import gdp_life_expectancy


@pytest.mark.parametrize('year', [
    '1900',
    '1920',
    '1929',
    '1939',
    '1945',
    '1960',
    '1995',
    '2010',
    '2024',
    '2050'
])
def test_gdp_life_expectancy_runs_without_errors(year):
    assert gdp_life_expectancy(year) is None


@pytest.mark.parametrize('year', [
    '-1',
    '2051',
    1995
])
def test_gdp_life_expectancy_no_entry(year):
    with pytest.raises(Exception):
        assert gdp_life_expectancy(year) is None

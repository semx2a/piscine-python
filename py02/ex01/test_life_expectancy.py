import pytest
from aff_life import life_expectancy


@pytest.mark.parametrize('country', [
    'France',
    'Armenia',
    'Bolivia',
    'Liberia',
    'Haiti',
    'Libya',
    'Russia',
    'Palestine',
    'China',
    'Turkey'
])
def life_expectancy_runs_without_errors(country):
    life_expectancy(country)


@pytest.mark.parametrize('country', [
    'Isnotreal'
])
def life_expectancy_no_entry(country):
    with pytest.raises(Exception):
        life_expectancy(country)
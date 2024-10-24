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
    'Turkey',
    'Dominica'
])
def test_life_expectancy_runs_without_errors(country):
    assert life_expectancy(country) is None


@pytest.mark.parametrize('country', [
    'Isnotreal',
    1
])
def test_life_expectancy_no_entry(country):
    with pytest.raises(Exception):
        assert life_expectancy(country) is None

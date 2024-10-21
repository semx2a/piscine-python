import pytest
from aff_pop import population_total


@pytest.mark.parametrize('country1, country2', [
    ('France', 'Germany'),
    ('Armenia', 'Greece'),
    ('Bolivia', 'Chile'),
    ('Haiti', 'Dominican Republic'),
    ('Libya', 'Egypt'),
    ('Russia', 'United States'),
    ('China', 'India')
])
def test_population_total_runs_without_errors(country1, country2):
    assert population_total(country1, country2) is None


@pytest.mark.parametrize('country1, country2', [
    ('Isnotreal', 'Palestine')
])
def test_population_total_no_entry(country1, country2):
    assert population_total(country1, country2) is None

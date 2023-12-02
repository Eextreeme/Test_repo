import pytest 
from laba5 import *


@pytest.fixture
def sample_countries():
    country1 = Country("USA", "Washington", "US", 331002651, 9833517, 21.43, GovernmentType.REPUBLIC)
    country2 = Country("China", "Beijing", "CN", 1444216107, 9596961, 16.2, GovernmentType.AOTOSHITISM)
    country3 = Country("India", "New Delhi", "IN", 1380004385, 3287263, 2.87, GovernmentType.DEMOCRACY)
    country4 = Country("Ukraine", "Kyiv", "UA", 40997699, 603550, 0.2, GovernmentType.DEMOCRACY)

    return country1, country2, country3, country4

@pytest.fixture
def sample_land(sample_countries):
    land = Land("Test Land")
    for country in sample_countries:
        land.add_country(country)
    return land

def test_init_country():
    country1 = Country("США", "Вашингтон", "US", 331002651, 9833517, 21.43, GovernmentType(2))
    assert country1.get_name() == "США" 

def test_calculate_population_density(sample_land):
    density_data = sample_land.calculate_population_density()
    assert len(density_data) == 4
    assert density_data[0][1] == pytest.approx(336.87, rel=1e-2)  # You might need to adjust the expected values

def test_sort_countries_by_gdp(sample_land):
    sorted_countries = sample_land.sort_countries_by_gdp()
    assert len(sorted_countries) == 4
    assert sorted_countries[0].get_name() == "USA"
    assert sorted_countries[1].get_name() == "China"

def test_select_country_by_population(sample_land):
    selected_countries = sample_land.select_country_by_population()
    assert len(selected_countries) == 2
    assert selected_countries[0].get_name() == "China"

def test_print_methods(capsys, sample_land):
    sample_land.print_countries()
    captured = capsys.readouterr()
    assert "USA" in captured.out

    sample_land.print_population_density()
    captured = capsys.readouterr()
    assert "Test Land" in captured.out

    sample_land.print_top_countries_by_gdp()
    captured = capsys.readouterr()
    assert "Топ країн за ВВП" in captured.out

    sample_land.print_countries_by_population()
    captured = capsys.readouterr()
    assert "Країни з населенням більше одного міліарда" in captured.out


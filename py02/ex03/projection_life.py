import os
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker as plticker

from load_csv import load

tens = dict(k=1e3, m=1e6, b=1e9)


def unpack_numbers():
    """
    unpack numbers is a lambda function based on a dict to translate
    abbreviated numbers forms (k, m, b) into integers
    """
    return (lambda x: int(float(x[0:-1]) * tens[x[-1].lower()]) if
            x[-1].isalpha() else int(x))


# format y axis to show numbers in thousands, millions, or billions
def format_func(value, ticks):
    """
    format func is a small utility function that takes a scientific notation
    and converts it to a float suffixed with an abbreviated number form, namely
    B = billion, M = million, k = thousand.
    """
    match value:
        case _ if value >= 1e9:
            return f'{value*1e-9:.1f}B'
        case _ if value >= 1e6:
            return f'{value*1e-6:.0f}M'
        case _ if value >= 1e3:
            return f'{value*1e-3:.1f}k'
        case _:
            return f'{value:.1f}'


def find_base(min_population: any, max_population: any) -> int:
    """
    find base is a small utility function that takes two values representing
    min and max values from a dataset representing total population, and
    returns a base to format the ticks interval of a plot.
    """
    range_population = max_population - min_population

    match range_population:
        case _ if range_population >= 1e9:
            return 200000000
        case _ if range_population >= 2e8:
            return 50000000
        case _ if range_population >= 1e8:
            return 20000000
        case _ if range_population >= 2e7:
            return 20000000
        case _ if range_population >= 1e7:
            return 3000000
        case _ if range_population >= 1e6:
            return 200000
        case _ if range_population >= 1e5:
            return 20000
        case _:
            return 2000


def render_plot(pop_over_years: pd.DataFrame, country_names: list) -> None:
    """
    `render plot` uses matplotlib and seaborn api functions to render a
    lineplot from a dataset and a list of country names.

    Parameters:
    pop_over_years: pd.DataFrame = Data Frame containing the data set to plot
    country_names: list = list of countries to plot

    Return Value:
    render_plot does not return any value.
    """
    # seaborn theme
    sns.set_theme()

    # plot settings with dataframe and column to axes values
    ax = sns.lineplot(
        data=pop_over_years,
        x='Year',
        y='Population',
        hue='Country'
    )

    # format plot text
    plt.title(f'Population Projection for {country_names[0]} and\
 {country_names[1]}', fontsize=15)
    plt.xlabel('Year', fontsize=10)
    plt.ylabel('Population', fontsize=10)
    plt.tick_params(axis='both', labelsize=8)

    # put a tick every 40 years on x axis
    xloc = plticker.MultipleLocator(base=40)
    ax.xaxis.set_major_locator(xloc)

    # format y axis ticks
    ax.yaxis.set_major_formatter(plt.FuncFormatter(format_func))
    # Determine the maximum population value to set the y-axis locator base
    max_pop = pop_over_years['Population'].max()
    min_pop = pop_over_years['Population'].min()
    yloc = plticker.MultipleLocator(find_base(min_pop, max_pop))
    ax.yaxis.set_major_locator(yloc)

    # show plot
    plt.show()


def gdp_life_expectancy(year: str) -> None:
    """
    `population_total` function loads the population_total.csv file and
    displays the total population of the selected countries. Manually changing
    the path results in undefined behavior.

    The data should be formated as such:
    |Country|year1|year2|..|yearN|
    |_______|_____|_____|__|_____|
    |France|pop1|pop2|...|popN|
    |..|..|..|..|..|

    Parameters:
    test_country: str = the name of the country to plot
    compare_country: str = the name of the country to compare

    Return value:
    None: the function returns None in all cases
    """
    try:
        abs_path = os.path.dirname(os.path.abspath(__file__))

        df_pop = load(os.path.join(abs_path, "../data/population_total.csv"))
        df_gdp = load(os.path.join(abs_path,
                                   "../data/income_per_person_gdppercapita_ppp_\
inflation_adjusted.csv"))

        if df_pop is None:
            raise RuntimeError('Data could not be loaded from population csv')

        if df_gdp is None:
            raise RuntimeError('Data could not be loaded from gdp csv')

        # Convert column values to list to make sure year value is available
        years = df_pop.columns.to_list()
        if year not in years:
            raise ValueError(f'{year} not found in population dataset')

        years = df_gdp.columns.to_list()
        if year not in years:
            raise ValueError(f'{year} not found in gdp dataset')

        # select and export corresponding columns
        fused_df = pd.DataFrame({'Country': df_pop['country'].tolist(),
                                   'Population': df_pop[year].tolist(),
                                   'GDP': df_gdp[year].tolist()})

        print(fused_df)

        # Slice country name from the list)
        # unpck = unpack_numbers()
        # test_country_pop = [unpck(pop) for pop in test_country_pop[1:]]
        # compare_country_pop = [unpck(pop) for pop in compare_country_pop[1:]]

        # Making new dataframe with cleaned data
        # cleaned_data = pd.DataFrame({'Year': years,
        #                            country_names[0]: test_country_pop,
        #                            country_names[1]: compare_country_pop})

        # Convert the dataframe from wide to long format
        # pop_over_years = pd.melt(cleaned_data, id_vars=['Year'],
        #                         value_vars=[country_names[0],
        #                                     country_names[1]],
        #                         var_name="Country",
        #                         value_name="Population")

        #print(pop_over_years)
        #render_plot(pop_over_years, country_names)

    except Exception as e:
        print(f'Exception: {e}')

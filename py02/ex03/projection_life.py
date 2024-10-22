import os
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
            not isinstance(x, int) and x[-1].isalpha() else int(x))


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


def find_base(min: any, max: any) -> int:
    """
    find base is a small utility function that takes two values representing
    min and max values from a dataset, and returns a base to format the ticks
    interval of a plot.
    """
    range = max - min

    match range:
        case _ if range >= 2e5:  # ie 200k
            return 50000
        case _ if range >= 1e5:  # ie 100k
            return 20000
        case _ if range >= 5e4:  # ie 50k
            return 10000
        case _ if range >= 1e4:  # ie 10k
            return 5000
        case _:
            return 2000


def render_plot(df_life_gdp: pd.DataFrame, year: str) -> None:
    """
    `render_plot` uses matplotlib and seaborn api functions to render a
    scatterplot from a dataset and a list of country names.

    Parameters:
    df_life_gdp: pd.DataFrame = Data Frame containing the data set to plot
    year: str = year to plot

    Return Value:
    render_plot does not return any value.
    """
    # seaborn theme
    sns.set_theme()

    # plot settings with dataframe and column to axes values
    sc = sns.scatterplot(
        data=df_life_gdp,
        x='GDP',
        y='Life Expectancy',
        hue='Country',
        legend=False
    )

    # format plot text
    plt.title(f'Relation between GDP and life expectancy in {year}',
              fontsize=15)
    plt.xlabel('GDP', fontsize=10)
    plt.ylabel('Life Expectancy', fontsize=10)
    plt.tick_params(axis='both', labelsize=8)

    # format x axis ticks
    sc.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
    # Determine the maximum population value to set the y-axis locator base
    max_life_gdp = df_life_gdp['GDP'].max()
    min_life_gdp = df_life_gdp['GDP'].min()
    xloc = plticker.MultipleLocator(find_base(min_life_gdp, max_life_gdp))
    sc.xaxis.set_major_locator(xloc)

    # show plot
    plt.show()


def gdp_life_expectancy(year: str) -> None:
    """
    `gdp_life_expectancy` function loads the life_expectancy_years.csv file and
    income_per_person_gdppercapita_ppp_inflation_adjusted.csv, and displays a
    plot of the relation between gdp and life expectancy in all countries in
    one year. Manually changing the path results in undefined behavior.

    Parameters:
    year: str = the year to plot

    Return value:
    None: the function returns None in all cases
    """
    try:
        abs_path = os.path.dirname(os.path.abspath(__file__))

        df_life = load(os.path.join(abs_path,
                                    "../data/life_expectancy_years.csv"))
        df_gdp = load(os.path.join(abs_path,
                                   "../data/income_per_person_gdppercapita_ppp_\
inflation_adjusted.csv"))

        if df_life is None:
            raise RuntimeError('Data could not be loaded from population csv')

        if df_gdp is None:
            raise RuntimeError('Data could not be loaded from gdp csv')

        # Convert column values to list to make sure year value is available
        years = df_life.columns.to_list()
        if year not in years:
            raise ValueError(f'{year} not found in population dataset')

        years = df_gdp.columns.to_list()
        if year not in years:
            raise ValueError(f'{year} not found in gdp dataset')

        # Slice country name from the list)
        unpck = unpack_numbers()
        ages = [float(age) for age in df_life[year].tolist()]
        gdprod = [unpck(gdp) for gdp in df_gdp[year].tolist()]

        # cleaning data
        df_life = pd.DataFrame({'Country': df_life['country'],
                                'Life Expectancy': ages})
        df_gdp = pd.DataFrame({'Country': df_gdp['country'],
                               'GDP': gdprod})

        # merging data and intersecting countries
        df_life_gdp = pd.merge(df_life,
                               df_gdp,
                               how='inner',
                               left_on='Country',
                               right_on='Country')

        # dropping NaN values and their corresponding row
        df_life_gdp = df_life_gdp.dropna()

        render_plot(df_life_gdp, year)

    except Exception:
        raise

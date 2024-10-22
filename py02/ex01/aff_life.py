import os
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker as plticker

from load_csv import load


def life_expectancy(country: str) -> None:
    """
    `life_expectancy` function loads the life_expectancy.csv file and displays
    the life expectancy of the selected country. Manually changing the path
    results in undefined behavior.

    The data should be formated as such:
    |Country|year1|year2|..|yearN|
    |_______|_____|_____|__|_____|
    |France|age1|age2|...|ageN|
    |..|..|..|..|..|

    Parameters:
    country: str = the name of the country to plot

    Return value:
    None: the function returns None in all cases
    """
    try:
        path = (os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             '../data/life_expectancy_years.csv'))
        df = load(path)

        if df is None:
            raise RuntimeError(f'Data could not be loaded from {path}')

        # check if country exists in dataframe
        if country not in df['country'].values:
            raise TypeError(f'{country} could not be found in Dataset')

        # select and export corresponding row
        country_data = df[df['country'] == country]

        # check if all values of the dataset are NaN
        if pd.isna(country_data.values[0][1:]).all():
            raise TypeError('No data available')

        # Convert column values to list
        years = country_data.columns.to_list()

        # Slice 'country' element to only keep year values
        years = [int(year) for year in years[1:]]

        # Turn values to list
        ages = country_data.values.tolist()

        # Slice country name element into a variable
        country_name = ages[0][0]

        # Turn list to numpy array
        ages = np.array(ages)

        # Flatten list from 2D to 1D array
        ages = ages.flatten()
        ages = ages.tolist()

        # Slice country name from the list)
        ages = [float(age) for age in ages[1:]]

        # Making new dataframe with cleaned data
        cleaned_data = {'Year': years, 'Life Expectancy': ages}
        life_expectancy = pd.DataFrame(cleaned_data)

        # set sns theme
        sns.set_theme()

        # create a plot / `ax` stands for `axes`
        ax = sns.lineplot(
            data=life_expectancy,
            x='Year',
            y='Life Expectancy'
        )

        # format plot text
        plt.title(f'Life Expectancy Projection for {country_name}',
                  fontsize=15)
        plt.xlabel('Year', fontsize=10)
        plt.ylabel('Life Expectancy', fontsize=10)
        plt.tick_params(axis='both', labelsize=8)

        # put a tick every 40 years on x axis
        xloc = plticker.MultipleLocator(base=40)
        ax.xaxis.set_major_locator(xloc)

        # show plot
        plt.show()

    except Exception as e:
        print(f'Exception: {e}')

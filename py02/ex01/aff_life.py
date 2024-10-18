import os
import numpy as np
import pandas as pd
import seaborn as sns
from load_csv import load


def life_expectancy(country: str) -> None:

    try:
        df = load((os.path.join(os.path.dirname(os.path.abspath(__file__)),
                  '../data/life_expectancy_years.csv')))

        if df is None:
            return None

        country_data = df[df['country'] == country]
        print(country_data)

        # Convert column values to list
        years = country_data.columns.to_list()
        # Slice 'country' element to only keep year values
        years = years[1:]
        print(years)

        # Turn values to list
        ages = country_data.values.tolist()
        # Turn list to numpy array
        ages = np.array(ages)
        # Flatten list from 2D to 1D array
        ages = ages.flatten()
        ages = ages.tolist()
        # Slice country name from the list)
        ages = ages[1:]
        print(ages)

        cleaned_data = {'Year': years, 'Life Expectancy': ages}
        life_expectancy = pd.DataFrame(cleaned_data)
        print(life_expectancy)

        # set sns theme
        sns.set_theme()

        # create a visualization
        sns.lineplot(
            data=life_expectancy,
            x='Year',
            y='Life Expectancy'
        )

    except Exception as e:
        print(f'Exception: {e}')

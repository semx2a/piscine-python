import os
import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    load takes a csv file path and returns a data frame.

    Parameters:
    path (str): path of the csv file.

    Return Value:
    dataframe (Pandas DataFrame): a dataframe containing the csv's content.
    """
    try:
        # Load csv data into a dataframe
        if os.path.exists(path) is False:
            raise FileNotFoundError(f'Could not find file {path}')

        if path.endswith('.csv') is False:
            raise ValueError('Make sure your file is a CSV file.')

        dataframe = pd.read_csv(path)
        if dataframe.empty is True:
            raise pd.errors.EmptyDataError
        print(f'Loading dataset of dimensions {dataframe.shape}')
        return dataframe

    except pd.errors.EmptyDataError:
        print(f"Error: The file {path} is empty.")
        raise
    except pd.errors.ParserError:
        print(f"Error: The file {path} contains invalid data.")
        raise
    except ValueError as ve:
        print(ve)
        raise
    except FileNotFoundError as fnf:
        print(fnf)
        raise
    except Exception as e:
        print(f'Exception: {e}')
        raise

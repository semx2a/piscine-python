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
        dataframe = pd.read_csv(path)
        if dataframe.isnull().values.any():
            raise ValueError("CSV file contains malformed rows")
        print(f'Loading dataset of dimensions {dataframe.shape}')
        return dataframe

    except pd.errors.EmptyDataError:
        exit(f"Error: The file {path} is empty.")
    except pd.errors.ParserError:
        exit(f"Error: The file {path} contains invalid data.")
    except Exception as e:
        exit(f'Exception: {e}')

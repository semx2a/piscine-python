import pandas as pd


def load(path: str) -> pd.DataFrame:

    try:
        dataframe = pd.read_csv(path)
        print(f'Loading dataset of dimensions {dataframe.shape}')
        return dataframe

    except pd.errors.EmptyDataError as ede:
        print(f'Empty data: {ede}')
    except pd.errors.ParserWarning as pw:
        print(f'Parser Warning: {pw}')
    except pd.errors.IncompatibilityWarning as iw:
        print(f'Incompatibility Warning: {iw}')
    except UnicodeDecodeError as ude:
        print(f'Decoding error: {ude}')
    except Exception as e:
        print(f'Exception: {e}')

    return None

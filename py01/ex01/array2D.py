import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list of float pairs from the specified start index to the end
    index.
    Args:
        family (list): A list of pairs (lists) containing float values.
        start (int): The starting index for the slice.
        end (int): The ending index for the slice.
    Returns:
        list: A sliced list of pairs (lists) containing float values from the
        start to end index.
        Returns an empty list if the input is invalid or an exception occurs.
    Raises:
        Exception: If an error occurs during slicing, the exception message is
        printed.
    """

    try:
        if family is None or start is None or end is None:
            return []
        if (not all(len(pair) == 2 for pair in family) or
                not all(isinstance(item, float) for pair in family
                        for item in pair)):
            return []

        family_array = np.array(family)
        sliced_family = family_array[start:end]

        print(f'My shape is : {family_array.shape}')
        print(f'My new shape is: {sliced_family.shape}')

        return sliced_family.tolist()

    except Exception as e:
        exit(f'Exception: {e}')

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

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

    except Exception as msg:
        print(msg)

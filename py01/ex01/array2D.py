import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

    try:
        family_array = np.array(family)
        sliced_family = family_array[start:end]

        print(f'My shape is : {family_array.shape}')
        print(f'My new shape is: {sliced_family.shape}')

    except Exception as msg:
        print(msg)

    return sliced_family.tolist()

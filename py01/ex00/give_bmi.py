import numpy as np


# ufunc for bmi equation
def compute_bmi(height: int | float, weight: int | float) -> int | float:
    """Simple BMI equation ufunc function"""

    return weight / (height * height)


def is_limit(bmi: int | float, limit: int) -> bool:
    """Simple BMI limit function returning TRUE if BMI > limit, else FALSE"""
    return limit < round(bmi)


# mybmi is a numpy ufunc, taking a function, the number of arguments (arrays),
# and the number of output arrays
# Using ndarrays instead of lists optimizes runtime, ndaraays are up to
# 50x faster than python lists
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """give_bmi is a function taking two lists, height and weight,
and returning a list of computed bmi values"""

    height_array = np.array(height)
    weight_array = np.array(weight)

    mybmi = np.frompyfunc(compute_bmi, 2, 1)

    return list(mybmi(height_array, weight_array))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit is a function taking a list of BMIs and returning a list of
Boolean"""

    bmi_array = np.array(bmi)
    my_limit = np.frompyfunc(is_limit, 2, 1)
    return list(my_limit(bmi_array, limit))

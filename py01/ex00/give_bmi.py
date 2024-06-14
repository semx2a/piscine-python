import numpy


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    bmi = []
    bmi.append((weight[0] / height[0] * height[0]))
    bmi.append((weight[1] / height[1] * height[1]))

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    pass

def square(x: int | float) -> int | float:
    """square returns the square value of argument x.
    Parameters:
    x: can be an integer or a float."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """pow return the values x raised to the power of itself.
    Parameters:
    x: can be an integer or a float."""
    return x ** x


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        try:
            nonlocal count
            base = function(x)
            for i in range(count):
                base = function(base)
            count += 1
            return base
        except Exception as e:
            print(e)

    return inner

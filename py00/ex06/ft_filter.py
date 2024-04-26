from typing import Any, Callable, Iterable, T


def ft_filter(func: Callable[[T], Any], iterable: Iterable[T]):
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """

    return [word for word in iterable if func(word)]

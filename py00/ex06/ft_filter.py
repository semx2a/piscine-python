import typing as t


def ft_filter(func: t.Callable[[t.T], t.Any], iterable: t.Iterable[t.T]):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    return [word for word in iterable if func(word)]

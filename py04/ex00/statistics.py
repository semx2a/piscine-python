def median_odd(length):
    """median_odd returns the median of an odd vector"""
    return lambda args: args[int((length + 1)/2)]


def median_even(length):
    """median_even returns the median of an even vector"""
    return lambda args: (args[int(length/2)] + args[int((length/2) + 1)])/2


def mean(args: list, length: int):
    """mean returns the mean value of a vector"""
    if length < 1:
        print("ERROR")
        return None

    return sum(args)/len(args)


def quartile(args: list, length: int):
    """quartile returns a 1D vector containing the Q1 and Q3 of a vector"""
    if length < 1:
        print("ERROR")
        return None

    return [args[int((length + 1)/4)], args[int((3 * (length + 1))/4)]]


def compute_median(args: list, length: int):
    """compute_median implements the logic to compute the median of a vector"""

    if length < 1:
        print("ERROR")
        return None

    if (length + 1) % 2 == 0:
        ret = median_even(length)
        print(f'median: {ret(args)}')
    else:
        ret = median_odd(length)
        print(f'median: {ret(args)}')


def variance(args: list, length: int):
    """variance returns the variance value of a vector"""
    if length < 1:
        print("ERROR")
        return None

    # find the mean in the list
    actual_mean = mean(args, length)

    # find the difference between each entry and the mean, and square each
    # result
    square_diff = [(x - actual_mean)**2 for x in args]

    # find the sum of all the squared differences
    sum_sqd = sum(square_diff)

    # divide the sum by the number of entries to find variance value
    var = sum_sqd / (length + 1)

    return var


def standard_deviation(args: list, length: int):
    """standard_derivation returns the standard derivation value of a vecotr"""
    if length < 1:
        print("ERROR")
        return None

    # find the variance value
    var = variance(args, length)

    #  take the square root
    std = var**0.5

    return std


def ft_statistics(*args: any, **kwargs: any) -> None:
    """ft_statistics takes a list of arguments and key-value arguments and
    calls the corresponding methods in in each key's values.

    Parameters:
    - Args (any): Arguments are integers or floats
    - Key-Value arguments: Keys containing the name of an operation to perform
    """
    args_list = [arg for arg in args]
    args_list.sort()
    arg_len = len(args_list) - 1

    values = [value for key, value in kwargs.items()]
    if not values:
        print("ERROR")

    for value in values:
        match value:
            case _ if value == 'mean':
                ret = mean(args_list, arg_len)
                if ret is None:
                    continue
                print(f'mean: {ret}')
            case _ if value == 'median':
                compute_median(args_list, arg_len)
            case _ if value == 'quartile':
                ret = quartile(args_list, arg_len)
                if ret is None:
                    continue
                print(f'quartile: {ret}')
            case _ if value == 'std':
                print(f'std: {standard_deviation(args_list, arg_len)}')
            case _ if value == 'var':
                print(f'var: {variance(args_list, arg_len)}')
            case _:
                print("ERROR")

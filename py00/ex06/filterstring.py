import sys
import string
from ft_filter import ft_filter


def is_needle(haystack: str):
    """is_needle() returns a lambda function to test if needle is in
haystack."""
    return lambda needle: needle in haystack


def not_printable():
    """not_printable() returns a lambda function to test if the character
is not printable."""
    return lambda char: char not in string.printable


def is_greater(size: int):
    """is_greater() returns a lambda function to test if the word's length is
greater than the size."""
    return lambda word: len(word) > size


def parse_string(S: str) -> None:
    """The parse_string() function tests the string for punctuation and
non printable characters. If either are found, the function raises an
AssertionError."""
    is_punctuation = is_needle(string.punctuation)
    isnot_printable = not_printable()

    punctuation_list = ft_filter(is_punctuation, S)
    invisible_list = ft_filter(isnot_printable, S)

    assert len(punctuation_list) == 0 \
        and len(invisible_list) == 0, "the arguments are bad"


def filterstring(S: str, N: int) -> list:
    """The filterstring() function returns a list of words from S that have a
length greater than N. The functions accepts two arguments:
- a string 'S''
- an integer 'N'
A word is separated by whitespaces."""
    parse_string(S)

    words_list = S.split()
    condition = is_greater(N)

    filtered_list = ft_filter(condition, words_list)

    return filtered_list


def main(argv):

    try:
        assert len(argv) == 3 \
            and argv[1].isascii() \
            and argv[2].isnumeric(), "the arguments are bad"

        filtered_list = filterstring(argv[1], int(argv[2]))
        print(filtered_list)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        exit(1)


if __name__ == "__main__":
    main(sys.argv)

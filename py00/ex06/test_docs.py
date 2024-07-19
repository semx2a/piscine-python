from ft_filter import ft_filter
import filterstring as fs


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def print_title(msg: str):
    print(f'{color.BOLD}{msg}{color.END}')


def main():

    print_title('filter doc:')
    print(f'{filter.__doc__}\n')
    print_title('ft_filter doc:')
    print(f'{ft_filter.__doc__}\n')
    print_title('filterstring doc:')
    print(f'{fs.filterstring.__doc__}\n')
    print_title('parse_string doc:')
    print(f'{fs.parse_string.__doc__}\n')
    print_title('is_greater doc:')
    print(f'{fs.is_greater.__doc__}\n')
    print_title('not_printable doc:')
    print(f'{fs.not_printable.__doc__}\n')
    print_title('is_needle doc:')
    print(f'{fs.is_needle.__doc__}\n')

    return 0


if __name__ == "__main__":
    main()

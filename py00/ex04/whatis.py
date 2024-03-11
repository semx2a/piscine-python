import sys


def whatis():
    lambda number: print("I'm Even.") if number % 2 == 0 else print("I'm Odd.")


def main(argv):
    try:
        assert len(argv) <= 2, "more than one argument provided"
        if len(argv) > 1:
            assert argv[1][0] == "-" and argv[1][1:].isnumeric() \
                or argv[1].isnumeric(), \
                "argument is not an integer"
            whatis(int(argv[1]))

    except AssertionError as msg:
        print(f'AssertionError: {msg}')
        exit(1)


if __name__ == "__main__":
    main(sys.argv)

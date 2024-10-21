import sys
import os

from rotate import ft_rotate


def main(av):
    try:
        assert len(av) == 2, "usage: __main__.py path/to/image"
        ft_rotate(av[1])
    except Exception as e:
        print(f"Exception: {e}")
        return 1
    return 0


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)

import sys
import os

from aff_pop import population_total


def main(av):
    try:
        assert len(av) == 3, "usage: __main__.py 'country_name'"
        population_total(av[1], av[2])
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

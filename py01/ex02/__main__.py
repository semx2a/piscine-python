from load_image import ft_load
import sys


def main(argv):
    try:
        assert len(argv) == 2, "usage: __main__.py path/to/image"
        print(ft_load(argv[1]))
    except Exception as e:
        exit(f"Exception: {e}")
    return 0


if __name__ == "__main__":
    main(sys.argv)

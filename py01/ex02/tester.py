from load_image import ft_load
import sys


def main(argv):
    try:
        assert len(argv) == 2, "usage: tester.py path/to/your/picture.jpg"
        print(ft_load(argv[1]))
    except Exception as e:
        print(f"{e}")
        return 1
    
    return 0

if __name__ == "__main__":
    main(sys.argv)

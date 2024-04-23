import sys
import string
import re


def print_result(args: tuple):
    """Printing of formatted args into a string"""

    assert len(args) == 6, "An error occured"

    result = f"The text contains {args[0]} characters:\n"
    result += f"{args[1]} upper letters\n"
    result += f"{args[2]} lower letters\n"
    result += f"{args[3]} punctuation marks\n"
    result += f"{args[4]} spaces\n"
    result += f"{args[5]} digits\n"

    print(result)


def parse_text(text: str):
    """Parses text into len values of different types of characters"""

    characters = len(text)
    uppercase = len(re.findall("[A-Z]", text))
    lowercase = len(re.findall("[a-z]", text))
    punctuation = len(re.findall("[" + string.punctuation + "]", text))
    spaces = len(re.findall("[" + string.whitespace + "]", text))
    digits = len(re.findall("[0-9]", text))

    return characters, uppercase, lowercase, punctuation, spaces, digits


def main(argv):
    try:
        assert len(argv) <= 2, \
            "Too many arguments! Usage: python building.py \"arg\" (optional)."

        if len(argv) == 1:
            print("What is the text to count?\n")
            text = sys.stdin.readline()
            # text = input("What is the text to count?\n")
        else:
            text = argv[1]
        
        print_result(parse_text(text))

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        exit(1)

    except (EOFError, KeyboardInterrupt):
        print("No data provided to input function")


if __name__ == "__main__":
    main(sys.argv)

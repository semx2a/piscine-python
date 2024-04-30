import sys

NESTED_MORSE = {" ": "/ ",
                "A": ".- ",
                "B": "_... ",
                "C": "-.-. ",
                "D": "-.. ",
                "E": ". ",
                "F": "..-. ",
                "G": "--. ",
                "H": ".... ",
                "I": ".. ",
                "J": ".--- ",
                "K": "-.- ",
                "L": ".-.. ",
                "M": "-- ",
                "N": "-. ",
                "O": "--- ",
                "P": ".--. ",
                "Q": "--.- ",
                "R": ".-. ",
                "S": "... ",
                "T": "- ",
                "U": "..- ",
                "V": "...- ",
                "W": ".-- ",
                "X": "-..- ",
                "Y": "-.-- ",
                "Z": "--.. ",
                "1": ".---- ",
                "2": "..--- ",
                "3": "...-- ",
                "4": "....- ",
                "5": "..... ",
                "6": "-.... ",
                "7": "--... ",
                "8": "---.. ",
                "9": "----. ",
                "0": "----- "}


def encrypt(message: str):

    encrypted_message = str()
    for char in message:
        encrypted_message += NESTED_MORSE[char.upper()]
    print(encrypted_message)


def main(argv):

    try:
        assert len(argv) == 2, "wrong number of arguments"
        assert all(chr.isalnum() or chr == ' ' for chr in argv[1]), \
            "only alphanumeric characters are allowed"

        encrypt(argv[1])

    except AssertionError as msg:
        print(f'AssertionError: {msg}')
    return 0


if __name__ == "__main__":
    main(sys.argv)

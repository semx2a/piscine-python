from give_bmi import give_bmi, apply_limit
import csv


def test(height: list[int | float], weight: list[float]) -> None:

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


def main():
    try:
        with open("unit_tests.csv", "r") as csvfile:

            dialect = csv.Sniffer().sniff(csvfile.read(1024), delimiters=",")
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect, lineterminator=",\n")

            height = []
            weight = []

            next(reader)  # skip header
            for row in reader:
                h, w = row[:2]  # unpack the first two elements
                height.extend([float(h) for h in h.split()])
                weight.extend([float(w) for w in w.split()])

        test(height, weight)

    except Exception as msg:
        print(f'Exception: {msg}')
    return 0


if __name__ == "__main__":
    main()

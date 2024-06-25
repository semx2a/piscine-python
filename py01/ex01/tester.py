from array2D import slice_me
from time import sleep


def test(family: list, start: int, end: int):
    print(f'Testing slice with start={start} and end={end}')
    print(slice_me(family, start, end))
    print()
    sleep(1)


def main():
    try:
        test_choice = 0

        while test_choice != 100:
            print('What test would you like to run?\n'
                  '1. Mandatory test\n'
                  '2. Extended test\n'
                  '3. Test with bigger family\n'
                  '100. Exit\n'
                  'Enter your choice: ', end='', flush=True)

            test_choice = int(input())
            print()

            if test_choice == 1 or test_choice == 2:
                family = [[1.80, 78.4],
                          [2.15, 102.7],
                          [2.10, 98.5],
                          [1.88, 75.2]]

                test(family, 0, 2)
                test(family, 1, -2)
                if test_choice == 2:
                    test(None, None, None)
                    test([], None, None)
                    test(family, None, 1)
                    test(family, 1, None)
                    test(family, 2, 4)
                    test(family, 3, 6)

            elif test_choice == 3:
                family = [[1.80, 78.4],
                          [2.15, 102.7],
                          [2.10, 98.5],
                          [1.88, 75.2],
                          [1.75, 65.9],
                          [1.77, 73.1],
                          [1.80, 82.1],
                          [1.85, 85.7],
                          [1.82, 79.2],
                          [1.75, 69.8]]

                test(None, None, None)
                test([], None, None)
                test(family, None, 1)
                test(family, 1, None)
                test(family, 0, 2)
                test(family, 1, -2)
                test(family, 2, 4)
                test(family, 3, 6)
                test(family, 4, 8)
                test(family, 5, 10)
                test(family, 6, 10)
            else:
                return 0

    except Exception as e:
        print(f'Error: {e}')
        return 1

    return 0


if __name__ == "__main__":
    main()

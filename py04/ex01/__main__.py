from in_out import outer
from in_out import square
from in_out import pow


def hello(x):
    pass


def main():
    try:

        my_counter = outer(3, square)
        print(my_counter())
        print(my_counter())
        print(my_counter())
        print("---")

        another_counter = outer(1.5, pow)
        print(another_counter())
        print(another_counter())
        print(another_counter())

        print("---")
        wrong_func = outer(3, hello)
        print(wrong_func())
        print(wrong_func())
        print(wrong_func())

        print("---")
        wrong_func1 = outer(3, "hello")
        print(wrong_func1())
        print(wrong_func1())
        print(wrong_func1())

        print("---")
        zero_count = outer(0, pow)
        print(zero_count())
        print(zero_count())
        print(zero_count())

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()

from callLimit import callLimit


def main():

    try:
        @callLimit(3)
        def f():
            print("f()")

        @callLimit(1)
        def g():
            print("g()")

        @callLimit(-1)
        def h():
            print("h()")

        @callLimit(2)
        def hello_world(message: str):
            print(message)

        var = "Hello World!"

        for i in range(3):
            f()
            g()
            h()
            hello_world(var)
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()

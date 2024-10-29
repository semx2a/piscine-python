class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print(f'Dot product is: {sum(x * y for x, y in zip(V1, V2))}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print(f'Add vector is: {[float(x + y) for x, y in zip(V1, V2)]}')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print(f'Sous vector is: {[float(x - y) for x, y in zip(V1, V2)]}')

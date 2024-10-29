from ft_calculator import calculator


def test_dotproduct(capsys):
    V1 = [1, 2, 3]
    V2 = [4, 5, 6]
    calculator.dotproduct(V1, V2)
    out, err = capsys.readouterr()
    assert out == "Dot product is: 32\n"


def test_add_vec(capsys):
    V1 = [1, 2, 3]
    V2 = [4, 5, 6]
    calculator.add_vec(V1, V2)
    out, err = capsys.readouterr()
    assert out == "Add vector is: [5.0, 7.0, 9.0]\n"


def test_sous_vec(capsys):
    V1 = [1, 2, 3]
    V2 = [4, 5, 6]
    calculator.sous_vec(V1, V2)
    out, err = capsys.readouterr()
    assert out == "Sous vector is: [-3.0, -3.0, -3.0]\n"

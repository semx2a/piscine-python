from array2D import slice_me
import pytest


@pytest.mark.parametrize("family, start, end, expected", [
    ([[1.80, 78.4],
      [2.15, 102.7],
      [2.10, 98.5],
      [1.88, 75.2]],
     0, 2,
     [[1.80, 78.4], [2.15, 102.7]]),  # family[0:2]

    ([[1.80, 78.4],
      [2.15, 102.7],
      [2.10, 98.5],
      [1.88, 75.2]],
     1, -2,
     [[2.15, 102.7]]),  # family[1:-2]

    ([[1.80, 78.4],
      [2.15, 102.7],
      [2.10, 98.5],
      [1.88, 75.2]],
     2, 4,
     [[2.10, 98.5], [1.88, 75.2]]),  # family[2:4]

    ([[1.80, 78.4],
      [2.15, 102.7],
      [2.10, 98.5],
      [1.88, 75.2]],
     3, 6,
     [[1.88, 75.2]])  # family[3:6] (6 is out of range, so it takes till the end)
])
def test_slice_me_ok(family, start, end, expected):
    assert slice_me(family, start, end) == expected


def test_slice_me_nok():

    assert slice_me(None, None, None) == []

    assert slice_me([[1.80, 78.4],
                    [2.15, 102.7],
                    [2.10, 98.5],
                    [1.88, 75.2]], None, None) == []

    assert slice_me([[1.80, 78.4],
                    [2.15, 102.7],
                    [2.10, 98.5],
                    [1.88, 75.2]], 2, None) == []

    assert slice_me([[1.80, 78.4],
                    [2.15, 102.7],
                    [2.10, 98.5],
                    [1.88, 75.2]], None, 2) == []

    assert slice_me([['hello', 78.4],
                    [2.15, 102.7],
                    [2.10, 98.5],
                    [1.88, 75.2]], 2, 4) == []

    assert slice_me([['1.80', '78.4'],
                    ['2.15', '102.7'],
                    ['2.10', '98.5'],
                    ['1.88', '75.2']], 2, 4) == []

    assert slice_me([[78.4],
                    [2.15, 102.7],
                    [2.10, 98.5],
                    [1.88, 75.2]], 2, 4) == []

    assert slice_me([[1.80, 78.4],
                    [2.15, 102.7],
                    [2.10, 98.5],
                    [1.88]], 2, 4) == []

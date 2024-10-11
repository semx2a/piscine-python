from give_bmi import give_bmi, apply_limit
import pytest


@pytest.mark.parametrize("heights, weights, expected", [
    ([2.71, 1.15, 1.84, 1.81, 1.0, -1.0, -1000.0, 1000.0],
     [165.3, 38.4, 73.0, 72.15, 2.0, -1.0, -2000.0, 2000.0],
     [22.507863455018317, 29.0359168241966, 21.561909262759922,
      22.023137266872197, 2.0, -1.0, -0.002, 0.002])
])
def test_give_bmi(heights, weights, expected):
    assert give_bmi(heights, weights) == expected


def test_give_bmi_strings():
    assert give_bmi(None, None) == []
    assert give_bmi([None, None, None], [None, None, None]) == []
    assert give_bmi([1, 2, 3], [1, 2, 3, 4]) == []
    assert give_bmi(['a', 'b', 'c'], ['d', 'e', 'f']) == []
    assert give_bmi(['ab', 'cd', 'ef'], ['gh', 'ij', 'kl']) == []


@pytest.mark.parametrize("bmi, limit, expected", [
    ([22.507863455018317, 29.0359168241966, 21.561909262759922,
      22.023137266872197, 2.0, -1.0, -0.002, 0.002],
     26,
     [False, True, False, False, False, False, False, False])
])
def test_apply_limit(bmi, limit, expected):
    assert apply_limit(bmi, limit) == expected


def test_apply_limit_fail():
    assert apply_limit(None, None) == []
    assert apply_limit([None, None, None], None) == []
    assert apply_limit([1, 2, 3], [4, 5, 6]) == []
    assert apply_limit(['a', 'b', 'c'], 'e') == []
    assert apply_limit(['ab', 'cd', 'ef'], 'gh') == []

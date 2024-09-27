from methods import dichotomy_method, golden_ratio_method, fibonacci_method


def test_dichotomy_method():
    assert [round(x, 2) for x in dichotomy_method()] == [-0.37, 1.16, 3.31]


def test_golden_ratio_method():
    assert [round(x, 2) for x in golden_ratio_method()] == [-0.37, 1.16, 3.31]


def test_fibonacci_method():
    assert [round(x, 2) for x in fibonacci_method()] == [-0.37, 1.16, 3.31]

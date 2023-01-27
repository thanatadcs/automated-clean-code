import automated_clean_code


def test_sanity():
    assert 1 + 1 == 2


def test_add():
    assert automated_clean_code.add_numbers(1, 2) == 3


"""
Just automated_clean_code.subtract_numbers(1, 1) without assert is cheating
line coverage is a necessary condition, but not sufficient
you need assert too
Another way to cheat is "git commit -n"
"""


def test_subtract():
    assert automated_clean_code.subtract_numbers(1, 1) == 0  # pragma: no cover

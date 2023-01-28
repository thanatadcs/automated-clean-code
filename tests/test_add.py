import sys
from os.path import dirname, join
from typing import Callable

import automated_clean_code
from automated_clean_code.exercise_20_histlib import (
    count_line_occurence,
    find_max_min_keys,
    get_filename_from_args,
    print_max_min_line_occurrence_from_file,
)


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


def test_find_max_min_keys():
    counter = {"hi": 3, "Hello World!": 1, "Not really": 9, "sad": 69}
    assert find_max_min_keys(counter) == (69, "sad", 1, "Hello World!")


def test_count_line_occurence():
    txt = "1\n2\n2\n3\n3\n3\n"
    expected = {"1": 1, "2": 2, "3": 3}
    assert count_line_occurence(txt) == expected


def test_simple_file(simple_test_data_file: str):
    assert simple_test_data_file == join(dirname(__file__), "./fixtures/hello.txt")


def test_get_filename_from_args():
    assert get_filename_from_args(["hello.py"]) == "hello.py"


def test_myoutput(capsys: Callable):
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"


def test_print_max_min_line_occurrence_from_file(capsys: Callable, simple_test_data_file: str):
    print_max_min_line_occurrence_from_file(simple_test_data_file)
    captured = capsys.readouterr()
    expected = "Min Key = 1 with count = 1\nMax Key = 3 with count = 3\n"
    assert captured.out == expected

# For this exercise focus on how to testability. How do we test thing like this?
# and test fixture
# the example data is in data/exercise20_data.txt
import argparse
import sys
from typing import Dict, List, Tuple


def main():
    """

    Print something.

    Returns: None

    """
    print_max_min_line_occurrence_from_args(sys.argv)


def print_max_min_line_occurrence_from_args(args: List[str]):
    """

    Print something.

    Returns: None

    """
    filename = get_filename_from_args(args)
    print_max_min_line_occurrence_from_file(filename)


def print_max_min_line_occurrence_from_file(filename: str):
    """

    Do something.

    Return: something

    """
    # fill up histogram
    with open(filename, "r") as lines:
        counter = count_line_occurence(lines)

        # find max key
        max_counter, max_key, min_counter, min_key = find_max_min_keys(counter)

        print(f"Min Key = {min_key} with count = {min_counter}")
        print(f"Max Key = {max_key} with count = {max_counter}")


def get_filename_from_args(args: List[str]) -> str:
    """

    Do something.

    Return: something

    """
    parser = argparse.ArgumentParser(
        description="compute the entry with the most occurrence and the least occurrence form a file"
    )
    parser.add_argument("filename")
    parsed_args = parser.parse_args(args)
    return parsed_args.filename


def count_line_occurence(lines: str) -> Dict[str, int]:
    """

    Do something.

    Return: something

    """
    counter = {}
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        if line in counter:
            counter[line] += 1
        else:
            counter[line] = 1
    return counter


def find_max_min_keys(counter: Dict[str, int]) -> Tuple[int, str, int, str]:
    """

    Do something.

    Return: something

    """
    max_key, min_key = None, None
    max_counter, min_counter = 0, 0
    for k, v in counter.items():
        if max_key is None or v > max_counter:
            max_key = k
            max_counter = v
        if min_key is None or v < min_counter:
            min_key = k
            min_counter = v
    return max_counter, max_key, min_counter, min_key


if __name__ == "__main__":
    main()

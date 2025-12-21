#!/usr/bin/env python3
import sys
import re


# *** SOLUTIONS ***
def parse(input_puzzle: str):
    lines = input_puzzle.strip().split("\n")
    ranges = []
    numbers = []
    for line in lines:
        if re.match(r"[0-9]+-[0-9]+", line):
            # print("range line")
            ranges.append(list(map(int, line.split("-"))))
        elif re.match(r"[0-9]+", line):
            # print("number line")
            numbers.append(int(line))
    return (ranges, numbers)


def part1(input_data: str):
    ranges, numbers = parse(input_data)
    print(ranges, numbers)

    count = 0
    for num in numbers:
        for start, end in ranges:
            print(start, end)
            if start <= num <= end:
                count += 1
                break
    return count


def part2(input_data: str):
    ranges, _ = parse(input_data)
    #print(ranges)

    # Merge the overlapped ranges.
    merged_ranges = []
    ranges.sort()
    for range in ranges:
        #print(range)
        if len(merged_ranges) == 0:
            merged_ranges.append(range)
            continue

        start, end = merged_ranges[-1]
        if end < range[0]:
            merged_ranges.append(range)
        elif end < range[1]:
            merged_ranges[-1] = [start, range[1]]
        #print(merged_ranges)

    count = sum([end - start + 1 for start, end in merged_ranges])
    return count


# *** TESTCASE ***
import unittest


class TestSolution(unittest.TestCase):
    def test_part1(self):
        input_str, exp = (
            """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""",
            3,
        )
        self.assertIsNotNone(exp)

        act = part1(input_str)
        self.assertEqual(exp, act)

    def test_part2(self):
        input_str, exp = (
            """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""",
            14,
        )
        self.assertIsNotNone(exp)

        act = part2(input_str)
        self.assertEqual(exp, act)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
import sys
import re

# *** SOLUTIONS ***
"""
The safe has dial from 0 to 99 and start point is 50.
"""


def parse(input_puzzle: str) -> [[]]:
    data = []
    lines = input_puzzle.strip().split("\n")
    for line in lines:
        assert re.match(r"L|R[0-9]+", line)
        # 'R' is 1, 'L' is -1
        direct = 1 if line[0] == "R" else -1
        data.append([direct, int(line[1:])])  # [1 or -1, number]
    # print(data)
    return data


def part1(input_data: str):
    data: [[]] = parse(input_data)

    point = 50
    cnt = 0
    for direct, num in data:
        point += direct * num
        point %= 100
        if point == 0:
            cnt += 1
    return cnt


def part2(input_data: str):
    point = 50
    cnt = 0
    data: [[]] = parse(input_data)
    for direct, num in data:
        prev = point
        # print(direct, num, "====")
        # print(cnt, point)
        point += direct * num

        # num of times turned dial
        laps = int(num / 100)
        point -= 100 * laps * direct
        cnt += laps
        if direct == 1:  # Right
            if point > 100 and 100 > prev:
                cnt += 1
        else:  # Left
            if point < 0 and 0 < prev:
                cnt += 1

        point %= 100
        if point == 0:
            cnt += 1
        # print(cnt, point)
    return cnt


# *** TESTCASE ***
import unittest


class TestSolution(unittest.TestCase):
    def test_part1(self):
        input_str, exp = (
            """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""",
            3,
        )
        self.assertIsNotNone(exp)
        act = part1(input_str)
        self.assertEqual(exp, act)

    def test_part2(self):
        input_str, exp = (
            """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""",
            6,
        )
        self.assertIsNotNone(exp)

        act = part2(input_str)
        self.assertEqual(exp, act)


if __name__ == "main":
    unittest.main()

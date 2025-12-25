#!/usr/bin/env python3
import sys
from pprint import pp
from collections import deque
from functools import cache

# *** SOLUTIONS ***


def part1(input_data: str):
    grid = input_data.split("\n")
    # pp(grid)

    size_row = len(grid)
    beams = deque([(0, grid[0].index("S"))])
    # print(beams)
    timelines = []
    cnt = 0

    def add(i, j):
        if (i, j) in timelines:
            return
        timelines.append((i, j))
        beams.append((i, j))

    while len(beams) > 0:
        # print(beams)
        i, j = beams.popleft()
        if i == size_row - 1:
            continue
        match grid[i][j]:
            case "^":
                cnt += 1
                add(i + 1, j - 1)
                add(i + 1, j + 1)
            case "." | "S":
                add(i + 1, j)

    # print(searched)
    print(cnt)
    return cnt


def part2(input_data: str):
    grid = input_data.split("\n")
    size_row = len(grid)
    # pp(grid)

    @cache
    def solve(i, j):
        #print(i,j)
        if i >= size_row:
            return 1

        match grid[i][j]:
            case "^":
                return solve(i + 1, j - 1) + solve(i + 1, j + 1)
            case "." | "S":
                return solve(i + 1, j)
            case _:
                return 0

    i, j = 0, grid[0].index("S")
    return solve(i, j)


# *** TESTCASE ***
import unittest


class TestSolution(unittest.TestCase):
    def test_part1(self):
        input_str, exp = (
            """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""",
            21,
        )
        self.assertIsNotNone(exp)

        act = part1(input_str.strip("\n\r"))
        self.assertEqual(exp, act)

    def test_part2(self):
        input_str, exp = (
            """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""",
            40,
        )
        self.assertIsNotNone(exp)

        act = part2(input_str.strip("\n\r"))
        self.assertEqual(exp, act)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
import sys
import pprint
import copy


# *** SOLUTIONS ***
def parse(input_data: str):
    data = [list(line) for line in input_data.strip().split("\n")]
    return data


def print_state(state: list[list[str]]):
    for h in state:
        print("".join(h))
    print()


def remove_roll(state: list[list[str]]) -> list[list[str]]:
    height, width = len(state), len(state[0])
    area = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for row in range(height):
        for col in range(width):
            if state[row][col] != "@":
                continue

            cnt = 0
            for i, j in area:
                n_row = row + i
                n_col = col + j
                if 0 <= n_row < height and 0 <= n_col < width:
                    if state[n_row][n_col] == "@":
                        cnt += 1

            if cnt < 4:
                state[row][col] = "x"

    return state


def part1(input_data: str):
    state = parse(input_data)
    state = remove_roll(state)
    ans = sum(h.count("x") for h in state)
    return ans


def part2(input_data: str):
    state = parse(input_data)
    before_state: list[list[str]] = []
    removed = 0
    while before_state != state:
        # print_state(state)
        before_state = copy.deepcopy(state)
        state = remove_roll(state)
        removed += sum(h.count("x") for h in state)
        state = [["." if c == "x" else c for c in row] for row in state]

    return removed


# *** TESTCASE ***
import unittest


class TestSolution(unittest.TestCase):
    def test_part1(self):
        input_str, exp = (
            """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""",
            13,
        )

        act = part1(input_str)
        self.assertEqual(exp, act)

    def test_part2(self):
        input_str, exp = (
            """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""",
            43,
        )
        self.assertIsNotNone(exp)

        act = part2(input_str)
        self.assertEqual(exp, act)


if __name__ == "__main__":
    unittest.main()

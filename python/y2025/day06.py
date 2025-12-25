#!/usr/bin/env python3
import sys
from itertools import zip_longest
import pprint


# *** SOLUTIONS ***
def part1(input_data: str):
    lines = input_data.split("\n")
    lines = [line.split() for line in lines]
    calcs = list(zip(*lines))
    # print(calcs)

    return sum(eval(op.join(ns)) for *ns, op in calcs)


def part2(input_data: str):
    lines = input_data.split("\n")
    # pprint.pp(lines)
    lines = list(zip_longest(*lines, fillvalue=" "))
    # pprint.pp(lines)

    total = 0
    calc = ""
    op = ""
    for *data, _op in lines:
        num = "".join(data).strip()
        # print(num, "===")
        if num != "":
            if _op != " ":
                op = _op
            calc += num + op
        else:
            # end a group of calc
            total += eval(calc[:-1])
            calc = ""

    total += eval(calc[:-1])
    print(total)

    return total


# *** TESTCASE ***
import unittest


class TestSolution(unittest.TestCase):
    def test_part1(self):
        input_str, exp = (
            """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""",
            4277556,
        )
        self.assertIsNotNone(exp)

        act = part1(input_str.strip("\n\r"))
        self.assertEqual(exp, act)

    def test_part2(self):
        input_str, exp = (
            """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""",
            3263827,
        )
        self.assertIsNotNone(exp)
        act = part2(input_str.strip("\n\r"))
        self.assertEqual(exp, act)


if __name__ == "__main__":
    unittest.main()

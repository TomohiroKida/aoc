#!/usr/bin/env python3
import sys

# *** SOLUTIONS ***
def part1(input_ns: str):
  ans = 0
  for line in input_ns.strip().split('\n'):
    ns = list(map(int,line))
    max_index_1 = ns.index(max(ns[:-1]))
    max_index_2 = ns.index(max(ns[max_index_1+1:]))
    joltage = ns[max_index_1] * 10 +  ns[max_index_2]
    ans += joltage
  return ans

def part2(input_ns: str):
  total = 0
  for line in input_ns.strip().split('\n'):
    joltage = 0
    print(line)
    bank = list(map(int,line))
    for i in range(11):
      digit = max(bank[:i-11])
      bank = bank[bank.index(digit)+1:]
      joltage = joltage * 10 + digit
      #print(digit, bank)
    total += joltage * 10 + max(bank)
  return total


# *** TESTCASE ***
import unittest
class TestSolution(unittest.TestCase):
  def test_part1(self):
    input_str, exp = (
"""
987654321111111
811111111111119
234234234234278
818181911112111
""", 357)
    self.assertIsNotNone(exp)

    act = part1(input_str)
    self.assertEqual(exp, act)

  def test_part2(self):
    input_str, exp = (
"""
987654321111111
811111111111119
234234234234278
818181911112111
""", 3121910778619)
    self.assertIsNotNone(exp)

    act = part2(input_str)
    self.assertEqual(exp, act)

if __name__ == '__main__':
  unittest.main()

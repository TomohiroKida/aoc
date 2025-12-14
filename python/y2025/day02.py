#!/usr/bin/env python3

# *** SOLUTIONS ***
def parse(input_puzzle: str):
  return [list(map(int, line.split("-"))) for line in input_puzzle.split(",")]

def part1(input_data: str):
  data = parse(input_data)
  #print(data)
  cnt = 0
  for a, b in data:
    for n in range(a, b+1):
      s = str(n)
      w = s[:int(len(s)/2)]
      if s == w*2: cnt += n
  return cnt

def part2(input_data: str):
  data = parse(input_data)
  cnt = 0
  for a, b in data:
    for n in range(a, b+1):
      s = str(n)
      for i in range(1, int(len(s)/2)+1):
        w = s[:i]
        if s == w*int(len(s)/i):
          cnt += n
          break
  return cnt


# *** TESTCASE ***
import unittest
class TestSolution(unittest.TestCase):
  def test_part1(self):
    input_str, exp = (
"""
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
""", 1227775554)
    self.assertIsNotNone(exp)

    act = part1(input_str)
    self.assertEqual(exp, act)

  def test_part2(self):
    input_str, exp = (
"""
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
""", 4174379265)
    self.assertIsNotNone(exp)

    act = part2(input_str)
    self.assertEqual(exp, act)


if __name__ == "main":
  unittest.main()

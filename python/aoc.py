#!/usr/bin/env python3
import argparse
import importlib

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('year', help='year: yyyy'  , default='2025')
  parser.add_argument('day',  help='day: dd'     , default='00')
  parser.add_argument('part', type=int, help='part: 1 or 2', nargs='?', default=None)
  args = parser.parse_args()

  file_path = f'../data/{args.year}/{args.day}_input.txt'
  print(file_path)

  input_data = []
  with open(file_path, 'r') as f:
    input_data = f.read()

  module = importlib.import_module("y{}.day{}".format(args.year, args.day))
  if args.part == 1:
    print('part1: ', module.part1(input_data))
  elif args.part == 2:
    print('part2: ', module.part2(input_data))
  else:
    print('part1: ', module.part1(input_data))
    print('part2: ', module.part2(input_data))

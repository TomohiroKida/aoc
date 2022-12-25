import sys
from mylibs.parse import parse_groups

def main():
  lines = open(sys.argv[1], "r").read().strip().split('\n')
  for line in lines: print(line)
  print(solve1(lines))
  print(solve2(lines))

def solve1(lines):
  monkeys = parse_groups(lines)
  pass
def solve2(lines):
  pass

if __name__ == "__main__":
    main()

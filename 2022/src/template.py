import sys

def main():
  lines = open(sys.argv[1], "r").read().strip().split('\n')
  print(lines)
  print(solve1(lines))
  print(solve2(lines))

def solve1():
  pass
def solve2():
  pass

if __name__ == "__main__":
    main()

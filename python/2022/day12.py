import sys
import string
from mylibs.graph import Grid, Point, bfsearch

def main():
  lines = open(sys.argv[1], "r").read().strip().split('\n')
  for line in lines: print(line)
  print(solve1(lines))
  print(solve2(lines))

# S=0
# a-z=1-26
# E=27
def codepoint(c: str):
  if c == 'S':
    return 0
  elif c == 'E':
    return 27
  else:
    return string.ascii_lowercase.index(c)+1

def toGrid(lines):
  grid = Grid([[Point(x, y, codepoint(p)) for y, p in enumerate(l)] for x, l in enumerate(lines)])
  return grid

def solve1(lines):
  g = toGrid(lines)
  start = None
  ends = None
  for l in g.grid:
    for p in l:
      if p.value == 0:
        start = p
      if p.value == 27:
        end = p
        at_end = lambda node: node == end
        p.value = 26
  #s = next((p for l in g.grid for p in l if p.value == 0), None)
  #e = next((p for l in g.grid for p in l if p.value == 27), None)
  #print(g, s, e)
  ps = bfsearch(g, start, at_end, lambda src, dst: src+1 >= dst)
  #print([p for p in ps])
  print(''.join([chr(p.value+96) for p in ps]))
  return len(ps)-1

def solve2(lines):
  g = toGrid(lines)
  start = None
  ends = []
  for l in g.grid:
    for p in l:
      if p.value == 27:
        start = p
        p.value = 26
      if p.value == 1:
        ends.append(p)
        at_end = lambda node: node in ends
  ps = bfsearch(g, start, at_end, lambda src, dst: src <= dst+1)
  print(''.join([chr(p.value+96) for p in ps]))
  return len(ps)-1

if __name__ == "__main__":
    main()

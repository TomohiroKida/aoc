import sys
import string
from dataclasses import dataclass, field

def main():
  lines = open(sys.argv[1], "r").read().strip().split('\n')
  for line in lines: print(line)
  print(solve1(lines))
  print(solve2(lines))


@dataclass
class Point:
  x: int = 0
  y: int = 0
  value: int = 0


@dataclass
class Grid:
  grid: list[list[Point]] 

  def find_outofrange(self, x, y) -> bool:
    if x < 0 or x > len(self.grid)-1:
      return True
    if y < 0 or y > len(self.grid[x])-1:
      return True
    return False

  def find_neighbors(self, node: Point) -> list[Point]:
    x: int = node.x
    y: int = node.y
    neighbors: list[Point] = []
    for (nx, ny) in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
      if not self.find_outofrange(nx, ny): 
        neighbors.append(self.grid[nx][ny])
    return neighbors


def bfsearch(grid: Grid, start: Point, end: Point, find_func) -> list[Point]:
  que: list[Point] = [[start]]
  visited: list[Point] = []
  while que: 
    path: Point = que.pop(0)
    node: Point = path[-1]

    if node == end:
      return path

    if node not in visited:
      visited.append(node)
      for neighbor in grid.find_neighbors(node):
        if find_func(node.value, neighbor.value):
          que.append(path+[neighbor])

  return None


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
  for l in g.grid:
    for p in l:
      if p.value == 0:
        s = p
      elif p.value == 27:
        e = p
        p.value = 26
  #s = next((p for l in g.grid for p in l if p.value == 0), None)
  #e = next((p for l in g.grid for p in l if p.value == 27), None)
  #print(g, s, e)
  ps = bfsearch(g, s, e, lambda a, b: a+1 >=  b)
  #print([p for p in ps])
  #print(''.join([chr(p.value+96) for p in ps]))
  return len(ps)-1

def solve2(grid):
  pass

if __name__ == "__main__":
    main()



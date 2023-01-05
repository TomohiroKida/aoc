import sys
import string
from dataclasses import dataclass, field

def main():
  lines = open(sys.argv[1], "r").read().strip().split('\n')
  for line in lines: print(line)
  print(solve1(lines))
  print(solve2(lines))

class _Grid:
  def __init__(self, grid):
    self.grid: [(int)] = [[ord(p) for p in l] for l in grid]
    self.height: int = len(grid)
    self.width:  int = len(grid[0])
    self.start: (int) = self.search_point('S')
    self.end:   (int) = self.search_point('E')
    self.grid[self.start[0]][self.start[1]] = ord('a')
    self.grid[self.end[0]][self.end[1]] = ord('z')

  def search_point(self, point: str) -> (int):
    for h in range(self.height):
      for w in range(self.width):
        if self.grid[h][w] == ord(point):
          return (h, w)

  def outofrange(self, pos: (int)):
    h, w = pos
    if h < 0 or h > self.height-1:
      return True
    if w < 0 or w > self.width-1:
      return True
    return False

  # return high elevation
  def getelev(self, pos: [int]):
    h, w = pos
    return self.grid[h][w]

  # check if you can climb new_pos from now_pos
  def find_canclimb(self, now_pos: (int), new_pos: (int)):
    now = self.getelev(now_pos)
    if not self.outofrange(new_pos):
      new = self.getelev(new_pos)
      if now+1  >= new:
        return True
    return False

  # return up, down, left, right neighbors of now_pos
  def find_neighbors(self, now_pos: (int)) -> [(int)]:
    h, w = now_pos
    neighbors = []
    for (nh, nw) in (h-1, w), (h+1, w), (h, w-1), (h, w+1):
      if self.find_canclimb(now_pos, (nh, nw)): 
        neighbors.append((nh, nw))
    return neighbors

def _bfsearch(grid: _Grid, start: (int), end: (int)) -> list[(int)]:
  que: list[(int)] = [[start]]
  visited: list[(int)] = []
  while que: 
    path: Point = que.pop(0)
    node: Point = path[-1]

    if node == end:
      return path

    for neighbor in grid.find_neighbors(node):
      if neighbor not in visited:
        visited.append(neighbor)
        if grid.find_canclimb(node, neighbor):
          que.append(path+[neighbor])

  return []



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
  visited: list[Point] = [start]
  while que: 
    path: Point = que.pop(0)
    node: Point = path[-1]

    if node == end:
      return path

    for neighbor in grid.find_neighbors(node):
      if find_func(node.value, neighbor.value):
        if neighbor not in visited:
          visited.append(neighbor)
          que.append(path+[neighbor])

  return None


# S=0
# a-z=1-26
# E=27
def codepoint(c: str):
  if c == 'S':
    return 0
  elif c == 'E':
    return 26
  else:
    return string.ascii_lowercase.index(c)+1

def toGrid(lines):
  grid = Grid([[Point(x, y, codepoint(p)) for y, p in enumerate(l)] for x, l in enumerate(lines)])
  return grid

def solve1(lines):
  g = toGrid(lines)
  s = next((p for l in g.grid for p in l if p.value == 0), None)
  e = next((p for l in g.grid for p in l if p.value == 26), None)
  print(g, s, e)
  ps = bfsearch(g, s, e, lambda a, b: a+1 >=  b)
  #print(''.join([chr(p.value+96) for p in ps]))
  print([(p.x, p.y) for p in ps])
  print(len(ps))

  grid = _Grid(lines)
  #print(grid.height, grid.width)
  #print(grid.start)
  #print(grid.end)
  p = _bfsearch(grid, grid.start, grid.end)
  #print(''.join([chr(grid.getelev(pp)) for pp in p])
  print([pp for pp in p])
  print(len(p)-1)

  return len(ps)

def solve2(grid):
  pass

if __name__ == "__main__":
    main()



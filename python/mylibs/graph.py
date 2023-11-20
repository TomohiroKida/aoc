from dataclasses import dataclass, field

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


def bfsearch(grid: Grid, start: Point, at_end, find_func) -> list[Point]:
  que: list[Point] = [[start]]
  visited: list[Point] = []
  while que: 
    path: Point = que.pop(0)
    node: Point = path[-1]

    if at_end(node):
      return path

    if node not in visited:
      visited.append(node)
      for neighbor in grid.find_neighbors(node):
        if find_func(node.value, neighbor.value):
          que.append(path+[neighbor])

  return None

import sys
from mylibs.graph import Point, Grid
from dataclasses import dataclass, field
from itertools import count

def main():
  lines = open(sys.argv[1], "r").read().strip().split('\n')
  for line in lines: print(line)
  print(solve1(lines))
  print(solve2(lines))

def parse(_lines):
  rock_info: list[[Point]] = []
  lines = [l.split('->') for l in _lines]
  for ls in lines:
    points: list[Point] = []
    for l in ls:
      pt = l.strip().split(',')
      point = Point(int(pt[0]), int(pt[1]))
      points.append(point)
    rock_info.append(points)
  return rock_info

@dataclass
class RockGrid(Grid):
  def __init__(self, min_pt, max_pt, sand_pos):
    self.debug = False
    self.range_pt = Point(max_pt.x - min_pt.x + (max_pt.y * 2 + 1), max_pt.y+2)
    #print(self.range_pt)
    self.grid = [['.'] * self.range_pt.x for i in range(self.range_pt.y)]
    self.offset_x = min_pt.x - max_pt.y 
    print(self.offset_x, len(self.grid), len(self.grid[0]))

    # put sand point
    self.sand_pos = Point(sand_pos.x-self.offset_x, sand_pos.y)
    self.put_obj(self.sand_pos.x, self.sand_pos.y, '+') 

  def put_rock(self, rock_info):
    for rocks in rock_info:
      for i in range(len(rocks)-1):
        xs = sorted([rocks[i].x, rocks[i+1].x])
        ys = sorted([rocks[i].y, rocks[i+1].y])
        #print(xs, ys)
        if xs[0] == xs[1]:
          for y in range(ys[0], ys[1]+1):
            self.grid[y][xs[0]-self.offset_x] = '#'
        else:
          for x in range(xs[0], xs[1]+1):
            self.grid[ys[0]][x-self.offset_x] = '#'

  def put_obj(self, x, y, obj):
    self.grid[y][x] = obj

  def display(self):
    if self.debug:
      for l in self.grid: 
        print(''.join(l))
      print()
    else:
      pass

  def move(self, x: int, y: int) -> Point:
    nx, ny = x, y
    if self.grid[y+1][x] == '.':
      ny = y + 1
      self.grid[y][x] = '.'
      self.grid[ny][nx] = 'o'
    elif self.grid[y+1][x] in '#o':
      if self.grid[y+1][x-1] == '.':
        nx = x - 1
        ny = y + 1
        self.grid[y][x] = '.'
        self.grid[ny][nx] = 'o'
      elif self.grid[y+1][x+1] == '.':
        nx = x + 1
        ny = y + 1
        self.grid[y][x] = '.'
        self.grid[ny][nx] = 'o'
    return Point(nx, ny)

  def step(self):
    # fall sand
    self.put_obj(self.sand_pos.x, self.sand_pos.y, 'o') 
    self.display()

    sand = Point(self.sand_pos.x, self.sand_pos.y)
    cnt = 0
    while True:
      #print(sand.x, sand.y)
      n_sand = self.move(sand.x, sand.y)
      cnt+=1
      self.put_obj(self.sand_pos.x, self.sand_pos.y, '+') 
      self.display()

      # finish condition
      if n_sand.y == self.range_pt.y-1:
        return False

      # no update sand state
      if n_sand == sand:
        break
      sand = n_sand
    if cnt < 2:
      return False

    return True

def solve1(lines):
  rock_info = parse(lines)
  max_pt = Point(max([l.x for ls in rock_info for l in ls]),
                 max([l.y for ls in rock_info for l in ls]))
  min_pt = Point(min([l.x for ls in rock_info for l in ls]),
                 min([l.y for ls in rock_info for l in ls]))
  print('min:', min_pt, 'max:', max_pt)
  sand_pos = Point(500, 0)
  grid = RockGrid(min_pt, max_pt, sand_pos)
  grid.put_rock(rock_info)
  grid.display()
  for i in count():
    if not grid.step():
      grid.display()
      return i

def solve2(lines):
  rock_info = parse(lines)
  max_pt = Point(max([l.x for ls in rock_info for l in ls])+1,
                 max([l.y for ls in rock_info for l in ls])+1)
  min_pt = Point(min([l.x for ls in rock_info for l in ls]),
                 min([l.y for ls in rock_info for l in ls]))
  print('min:', min_pt, 'max:', max_pt)
  sand_pos = Point(500, 0)
  grid = RockGrid(min_pt, max_pt, sand_pos)

  # add floor
  for i in range(grid.range_pt.x):
    grid.put_obj(i, max_pt.y+1, '#')

  # add rock
  grid.put_rock(rock_info)

  grid.display()

  # step
  for i in count():
    if not grid.step():
      return i+1

if __name__ == "__main__":
    main()

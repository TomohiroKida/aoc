import sys

def main():
  lines = open(sys.argv[1], "r").read().strip().split('\n')
  for line in lines: print(line)
  print(solve1(lines))
  print(solve2(lines))

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __eq__(self, other):
    if not isinstance(other, Point):
      return NotImplemented
    return self.x == other.x and self.y == other.y

def parse_motions(lines):
  motions = []
  for line in lines:
    way, step = line.split(' ')
    motions.append([way, int(step)])
  return motions

def move_head(knot: Point, way: str) -> Point:
  if way == 'L':
    return Point(knot.x-1, knot.y)
  elif way == 'R':
    return Point(knot.x+1, knot.y)
  elif way == 'U':
    return Point(knot.x, knot.y+1)
  elif way == 'D':
    return Point(knot.x, knot.y-1)
  else:
    return Point(kx, ky)

def move_tail(head: Point, tail: Point) -> Point:
  vx, vy = (head.x-tail.x), (head.y-tail.y)
  dx, dy = abs(vx), abs(vy)
  update = Point(0, 0)
  # same line
  if dx >= 2 and dy == 0:
    update.x = vx/abs(vx)
  elif dy >= 2 and dx == 0:
    update.y = vy/abs(vy)
  # ohter
  elif dx + dy > 2:
    update.x = vx/abs(vx)
    update.y = vy/abs(vy)
  return Point(int(tail.x+update.x), int(tail.y+update.y))

def solve1(lines):
  motions = parse_motions(lines)
  head = Point(0, 0)
  tail = Point(0, 0)
  #print('(%d, %d), (%d, %d)' % (hx, hy, tx, ty))
  stamp = []
  for motion in motions:
    way: str = motion[0]
    step: int = motion[1]
    #print('# %s %s' % (way, step))
    for i in range(step):
      head = move_head(head, way)
      tail = move_tail(head, tail)
      if not tail in stamp:
        stamp.append(tail)
  return len(stamp)

def solve2(lines):
  motions = parse_motions(lines)
  knots = [Point(0, 0)] * 10
  stamp = []
  for motion in motions:
    way: str = motion[0]
    step: int = motion[1]
    #print('# %s %s' % (way, step))
    for i in range(step):
      knots[0] = move_head(knots[0], way)
      for x in range(1, 10):
        knots[x] = move_tail(knots[x-1], knots[x])
      if not knots[9] in stamp:
        stamp.append(knots[9])
  return len(stamp)

if __name__ == "__main__":
    main()

class Octopuse:
  def __init__ (self, inputs):
    self.oct_map = inputs 

  def display(self):
    for i in range(10):
      for j in range(10):
        p = self.oct_map[i][j]
        if p == 0:
          print('\033[1m' + str(p) + '\033[0m', end='')
        else:
          print(p, end='')
      print('\n', end='')
    print()

  def step(self):
    # *** Increase by 1 ***
    n1_oct_map = [[0 for x in range(10)] for y in range(10)]
    for i in range(10):
      for j in range(10):
        n1_oct_map[i][j] = self.oct_map[i][j] + 1

    # *** Check if oct flashed ***
    flashed_oct = [[False for x in range(10)] for y in range(10)]
    while True:
      flash_now = False
      for i in range(10):
        for j in range(10):

          # flashing now
          if n1_oct_map[i][j] > 9 and not flashed_oct[i][j]:
            flash_now = True
            flashed_oct[i][j] = True

            # update around octs
            for xi in [-1, 0, 1]:
              for xj in [-1, 0, 1]:
                if i+xi < 0 or i+xi >= 10 or j+xj < 0 or j+xj >= 10:
                  continue
                n1_oct_map[i+xi][j+xj] += 1

      if not flash_now:
        break

    # *** Set flashe oct to 0 ***
    cnt_flash = 0
    for i in range(10):
      for j in range(10):
        if n1_oct_map[i][j] > 9:
          n1_oct_map[i][j] = 0
          cnt_flash += 1

    self.oct_map = n1_oct_map
    return cnt_flash

  # Check all of octs are flashing
  def is_synchronizing(self):
    for l in self.oct_map:
      for o in l: 
        if not o == 0:
          return False
    return True

# Return num of flashed octs during 100 steps
def solve1(octopuse_map):
  oct = Octopuse(octopuse_map)
  oct.display()

  cnt_flash = 0
  for i in range(100):
    print(i+1)
    cnt_flash += oct.step()
    oct.display()

  print(cnt_flash)

# Return num of steps if all of octs synchronizing for the first time
def solve2(octopuse_map):
  oct = Octopuse(octopuse_map)
  cnt = 0
  while True:
    cnt += 1
    oct.step()
    if oct.is_synchronizing():
      break

  print(cnt)

import sys
with open(sys.argv[1], "r") as f:
  inputs = f.read()
lines = inputs.strip().split('\n')
octopuse_map = [list(map(int, list(line))) for line in lines]
print(octopuse_map)

solve1(octopuse_map)
solve2(octopuse_map)


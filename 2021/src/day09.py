import fileinput
from functools import reduce

def func1(inputs):
  cnt = 0
  imax = len(inputs)
  jmax = len(inputs[0])
  for i in range(imax):
    for j in range(jmax):
      target  = inputs[i][j]
      up      = inputs[i-1][j] if i-1 > -1   else 9
      down    = inputs[i+1][j] if i+1 < imax else 9
      left    = inputs[i][j-1] if j-1 > -1   else 9
      right   = inputs[i][j+1] if j+1 < jmax else 9
      arounds = [up, down, left, right]
      if all(map(lambda around: around > target, arounds)):
        cnt += target + 1 
  print(cnt)

def is_bound_of_area(i, j, imax, jmax):
  if i >= 0 and i < imax and j >= 0 and j < jmax:
    return False
  else:
    return True 

def calc_basin_size(inputs, basin):
  i = basin[0]
  j = basin[-1]
  target = inputs[i][j]
  imax = len(inputs)
  jmax = len(inputs[0])
  arounds = [basin]
  for offset_i in [-1, 0, 1]:
    for offset_j in [-1, 0, 1]:
      if abs(offset_i) == abs(offset_j):
        continue
      around_i = i+offset_i
      around_j = j+offset_j
      if is_bound_of_area(around_i, around_j, imax, jmax):
        continue 
      around = inputs[around_i][around_j]
      if around == 9:
        continue
      if around > target:
        arounds += calc_basin_size(inputs, [around_i, around_j])
  return arounds

def func2(inputs):
  imax = len(inputs)
  jmax = len(inputs[0])

  basins = []
  for i in range(imax):
    for j in range(jmax):
      target  = inputs[i][j]
      up      = inputs[i-1][j] if i-1 > -1   else 9
      down    = inputs[i+1][j] if i+1 < imax else 9
      left    = inputs[i][j-1] if j-1 > -1   else 9
      right   = inputs[i][j+1] if j+1 < jmax else 9
      arounds = [up, down, left, right]
      if all(map(lambda around: around > target, arounds)):
        basins.append([i, j])

  list_basin_size = []
  for basin in basins:
    # [[x1, y1], [x2, y2], [x3, y3]]
    arounds = calc_basin_size(inputs, basin)
    list_basin_size.append(len(list(map(list, set(map(tuple, arounds))))))

  list_basin_size.sort(reverse = True)
  print(list_basin_size)
  print(reduce(lambda x, y: x * y, list_basin_size[0:3]))


inputs = [list(map(int, list(x.strip()))) for x in fileinput.input()]
print(inputs)
func1(inputs)
func2(inputs)

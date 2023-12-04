def solve1(sections):
  sumoverlap = 0
  for pair in sections:
    sec1, sec2 = pair
    f1, t1 = list(map(int, sec1.split('-')))
    f2, t2 = list(map(int, sec2.split('-')))
    if (f2 <= f1 and t1 <= t2) or \
       (f1 <= f2 and t2 <= t1):
      sumoverlap += 1
  print(sumoverlap)

def solve2(sections):
  sumnotoverlap = 0
  for pair in sections:
    sec1, sec2 = pair
    f1, t1 = list(map(int, sec1.split('-')))
    f2, t2 = list(map(int, sec2.split('-')))
    # f1-t1 f2-t2
    if (f1 < f2 and t1 < t2 and t1 < f2) or \
       (f2 < f1 and t2 < t1 and t2 < f1):
      sumnotoverlap += 1
  print(len(sections)-sumnotoverlap)

import sys
with open(sys.argv[1], "r") as f:
  inputs = f.read()
lines = inputs.strip().split('\n')
sections = [line.split(',') for line in lines]

solve1(sections)
solve2(sections)

def game(opp, you):
  # draw
  if you == opp:
    return 3 + you
  # win
  elif you - opp == 1 or \
       (you == 1 and opp == 3):
    return 6 + you
  # lose
  else:
    return 0 + you

def solve1(battles):
  chose_opp = {'A': 1, 'B': 2, 'C': 3}
  chose_you = {'X': 1, 'Y': 2, 'Z': 3}
  res = 0
  for battle in battles:
    opp, you = battle
    select_opp = chose_opp[opp]
    select_you = chose_you[you]
    print(select_opp, select_you)
    res += game(select_opp, select_you)
  print(res)

def solve2(battles):
  chose_opp = {'A': 1, 'B': 2, 'C': 3}
  chose_you = {'X': 1, 'Y': 2, 'Z': 3}
  res = 0
  for battle in battles:
    opp, you = battle
    select_opp = chose_opp[opp]
    # you must lose
    if you == 'X':
      select_you = select_opp - 1
      if select_opp == 1:
        select_you = 3
    # you must draw
    elif you == 'Y':
      select_you = select_opp 
    # you must win
    else:
      select_you = select_opp + 1
      if select_opp == 3:
        select_you = 1

    print(select_opp, select_you)
    res += game(select_opp, select_you)
  print(res)

import sys
with open(sys.argv[1], "r") as f:
  inputs = f.read()
lines = inputs.strip().split('\n')
battles = [l.split(' ') for l in lines]
print(battles)

solve1(battles)
solve2(battles)

def ascii2num(item):
  if item.islower():
    return ord(item) - 96
  else:
    return ord(item) - 38

def solve1(rucksacks):
  sum_priorities = 0
  for rucksack in rucksacks:
    print(rucksack)
    halfsize = int(len(rucksack)/2)
    compartment1 = rucksack[0:halfsize]
    compartment2 = rucksack[halfsize:]
    print(compartment1, compartment2)
    for item in compartment1:
      if item in compartment2:
        print(item, ord(item))
        sum_priorities += ascii2num(item)
        break
  print(sum_priorities)

def search_priority(group):
  print(group)
  for item in group[0]:
    include = True
    for rucksack in group[1:]:
      if not item in rucksack:
        include = False
        break
    if include:
      print(item)
      return ascii2num(item)

def solve2(rucksacks):
  sum_priorities = 0
  ruck_size = int(len(rucksacks))
  for i in range(0, ruck_size, 3):
    sum_priorities += search_priority(rucksacks[i:i+3])
  print(sum_priorities)

import sys
with open(sys.argv[1], "r") as f:
  inputs = f.read()
lines = inputs.strip().split('\n')
print(lines)

solve1(lines)
solve2(lines)

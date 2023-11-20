import sys
with open(sys.argv[1], "r") as f:
  inputs = f.read()
lines = inputs.strip().split('\n')
elves = [[]]
i = 0
for l in lines:
  if l == '':
    elves.append([])
    i += 1
  else:
    elves[i].append(int(l))
print(elves)
print(max([sum(elf) for elf in elves]))
print(sum(sorted([sum(elf) for elf in elves], reverse=True)[0:3]))

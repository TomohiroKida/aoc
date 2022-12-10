import sys
import re
import copy

def parse(lines):
  stack_str = []
  move_str = []
  num_crate  = 0
  for line in lines:
    if line == '':
      continue
    if re.match('^ 1', line):
      num_crate = list(map(int, line.strip().split('   ')))[-1]
    elif re.match('^move', line):
      move_str.append(line)
    else:
      stack_str.append(line)
  return num_crate, stack_str, move_str 

def parse_stack(num_crate, stack_str):
  stacks = []
  for i in range(num_crate):
    stacks.append([])

  stack_str.reverse()
  for line in stack_str:
    #print('#', line)
    for i in range(num_crate):
      #print(i*4+1)
      crate = line[i*4+1]
      if crate != ' ':
        stacks[i].append(crate)
  return stacks

def parse_move(move_str):
  moves = []
  for l in move_str:
    l = l.split(' ')
    n, f, t = l[1], l[3], l[5]
    moves.append([int(n), int(f)-1, int(t)-1])
  return moves

def solve1(_stacks, moves):
  stacks = copy.deepcopy(_stacks)
  for move in moves:
    num_crate, from_stack, to_stack = move
    for i in range(num_crate):
      crate = stacks[from_stack].pop()
      stacks[to_stack].append(crate)
      #print(stacks)
  print(''.join([stack.pop() for stack in stacks]))

def solve2(_stacks, moves):
  stacks = copy.deepcopy(_stacks)
  for move in moves:
    num_crate, from_stack, to_stack = move
    crates = []
    for i in range(num_crate):
      crates.append(stacks[from_stack].pop())
    for i in range(num_crate):
      stacks[to_stack].append(crates.pop())
      #print(stacks)
  print(''.join([stack.pop() for stack in stacks]))

## main ##

with open(sys.argv[1], "r") as f:
  inputs = f.read()
print(inputs)
lines = inputs.split('\n')

num_crate, stack_str, move_str = parse(lines)
#print(num_crate)

stacks = parse_stack(num_crate, stack_str)
#print(stacks)

moves = parse_move(move_str)
#print(moves)

solve1(stacks, moves)
solve2(stacks, moves)

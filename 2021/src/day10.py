def is_open_chunk(chunk):
  if chunk == '(' or chunk == '[' or chunk == '{' or chunk == '<' :
    return True
  else:
    return False

def is_complete(left_chunk, right_chunk):
  if (left_chunk == '(' and right_chunk == ')') or \
     (left_chunk == '[' and right_chunk == ']') or \
     (left_chunk == '{' and right_chunk == '}') or \
     (left_chunk == '<' and right_chunk == '>') :
    return True
  else:
    return False

def syntax_checker(line):
  stack = []
  for chunk in line:
    if is_open_chunk(chunk):
      stack.append(chunk)
    else:
      if len(stack) == 0:
        exit()
      if not is_complete(stack.pop(), chunk):
        return chunk
  return ''

def solve(lines):
  illegals = []
  for line in lines:
    char = syntax_checker(line)
    if char != '':
      illegals.append(char)
  point_list = {')': 3, ']': 57, '}': 1197, '>': 25137}
  points = [point_list[illegal] for illegal in illegals]
  print(sum(points))

import sys
with open(sys.argv[1], "r") as f:
  inputs = f.readlines()
lines = [x.strip() for x in inputs]
print(lines)
solve(lines)

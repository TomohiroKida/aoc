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
        return chunk, stack
  return '', stack

def solve1(lines):
  illegals = []
  for line in lines:
    #print(line)
    res, _ = syntax_checker(line)
    #print(res)
    if res != '':
      illegals.append(res)
  point_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
  points = [point_table[illegal] for illegal in illegals]
  print(sum(points))

def open2close(open_chunk):
  match open_chunk:
    case '(': return ')'
    case '[': return ']'
    case '{': return '}'
    case '<': return '>'

def solve2(lines):
  scores = []
  for line in lines:
    res , stack = syntax_checker(line)
    if res != '':
      continue

    adding = list(map(open2close, stack))
    adding.reverse()
    #print(adding)
    point_table = {')': 1, ']': 2, '}': 3, '>': 4}
    point_adding = [point_table[x] for x in adding]

    # calc score
    score = 0
    #print(point_adding)
    for value in point_adding:
      score = score * 5 + value
    #print(score)
    scores.append(score)

  # print middle score
  scores.sort()
  #print(scores)
  print(scores[int((len(scores)-1)/2)])
    
import sys
with open(sys.argv[1], "r") as f:
  inputs = f.readlines()
lines = [x.strip() for x in inputs]
solve1(lines)
solve2(lines)

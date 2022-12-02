import sys
import copy

def step(graph, passed, s, trace, max_visit):
  _passed = copy.deepcopy(passed)
  _trace = copy.deepcopy(trace)

  cnt = 0

  if _passed[s] == max_visit:
    return 0

  if s.islower():
    _passed[s] += 1
  _trace += s + ','

  if s == 'end':
    #print(_trace)
    return 1

  ns = graph[s]
  for n in ns:
    if _passed[n] == max_visit:
      continue
    cnt += step(graph, _passed, n, _trace, max_visit)

  return cnt

def solve1(graph, passed):
  trace = '' 
  cnt = step(graph, passed, 'start', trace, 1)
  print(cnt)

def solve2(graph, passed):
  trace = '' 
  cnt = step(graph, passed, 'start', trace, 2)
  print(cnt)

def connect(g, p, a, b):
  p[a] = 0
  if b == 'start' or a == 'end':
    return
  if a in g:
    g[a].append(b)
  else:
    g[a] = [b]

with open(sys.argv[1], "r") as f:
  inputs = f.read()
lines = inputs.strip().split('\n')
print(lines)

graph = {}
passed = {}
for line in lines:
  a, b = line.split('-')
  connect(graph, passed, a, b)
  connect(graph, passed, b, a)
  
print(graph)
print(passed)
solve1(graph, passed)
solve2(graph, passed)

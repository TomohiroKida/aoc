import sys

def main():
  lines = open(sys.argv[1], "r").read().strip().split('\n')
  lines = [list(map(int, list(x))) for x in lines]
  for line in lines:
    print(*line)
  print(solve1(lines))
  print(solve2(lines))

def isvisible(target_tree, next_trees):
  distance = 0
  for next_tree in next_trees:
    distance += 1
    if target_tree <= next_tree:
      break
  return distance

def solve1(lines):
  height = len(lines)
  width = len(lines[0])

  num_visible_tree = 0
  for h in range(1, height-1):
    for w in range(1, width-1):
      tt = lines[h][w]
      lv = tt > max([lines[h][l] for l in range(0, w)])
      rv = tt > max([lines[h][r] for r in range(w+1, width)])
      uv = tt > max([lines[u][w] for u in range(0, h)])
      dv = tt > max([lines[d][w] for d in range(h+1, height)])
      if(any([lv, rv, uv, dv])):
        num_visible_tree += 1

  num_edge_tree = height*2 + width*2 - 4
  return num_visible_tree + num_edge_tree

def solve2(lines):
  height = len(lines)
  width = len(lines[0])

  scores = [] 
  for h in range(1, height-1):
    for w in range(1, width-1):
      tt = lines[h][w]
      ls = isvisible(tt, [lines[h][l] for l in reversed(range(0, w))])
      rs = isvisible(tt, [lines[h][r] for r in range(w+1, width)])
      us = isvisible(tt, [lines[u][w] for u in reversed(range(0, h))])
      ds = isvisible(tt, [lines[d][w] for d in range(h+1, height)])
      score = ls * rs * us * ds
      scores.append(score)

  return max(scores)

if __name__ == "__main__":
    main()

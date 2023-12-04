import sys
from pathlib import Path
from collections import defaultdict

def main():
  lines = open(sys.argv[1], "r").read().strip().split('\n')
  print(lines)
  print(solve1(lines))
  print(solve2(lines))

def parse(lines):
  pwd  = Path('/')
  dirtree = defaultdict(dict) 
  for line in lines:
    #print("line:", line)
    token = line.split(' ')
    # [command]
    if token[0] == '$':
      command = token[1]
      if command == 'cd':
        dirname = token[2]
        if dirname == '..':
          pwd = pwd.parent
        else:
          pwd = pwd / dirname
    # dir [dirname]
    elif token[0] == 'dir':
      dirname = token[1]
      continue
    # size [filename]
    else:
      filesize = int(token[0])
      filename = token[1]
      dirtree[pwd][filename] = filesize
  return dirtree

def calcsizes(dirtree):
  sizes = defaultdict(int)
  for path in dirtree.keys():
    size = sum(dirtree[path].values())
    sizes[path] += size
    for parent in path.parents:
      sizes[parent] += size
  return sizes

def solve1(lines):
  dirtree = parse(lines)
  sizes = calcsizes(dirtree)

  return (sum([x for x in sizes.values() if x <= 100000]))

def solve2(lines):
  dirtree = parse(lines)
  sizes = calcsizes(dirtree)

  TOTAL_SPACE = 70000000
  UPDATE_SPACE = 30000000
  unused = TOTAL_SPACE - sizes[Path('/')]
  want = UPDATE_SPACE - unused

  for directory in sorted(sizes.values()):
    if want < directory:
      return directory

if __name__ == "__main__":
    main()

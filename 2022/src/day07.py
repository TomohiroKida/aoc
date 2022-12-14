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
  dirs = defaultdict(dict) 
  for line in lines:
    print("line:", line)
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
      dirs[pwd][filename] = filesize
  return dirs

def solve1(lines):
  dirs = parse(lines)
  print(dirs)

  sizes = defaultdict(int)
  for path in dirs.keys():
    size = sum(dirs[path].values())
    sizes[path] += size
    for parent in path.parents:
      sizes[parent] += size

  return (sum([x for x in sizes.values() if x <= 100000]))

def solve2(lines):
  pass


if __name__ == "__main__":
    main()

import sys

def solve(stream, bufsize):
  for i in range(len(stream)):
    buf = stream[i:i+bufsize]
    if not len(buf) == bufsize:
      break
    sorted_buf = sorted(buf)
    if len(set(sorted_buf)) == bufsize:
      print(buf, i+bufsize)
      break

with open(sys.argv[1], "r") as f:
  inputs = f.read()
solve(inputs.strip(), 4)
solve(inputs.strip(), 14)

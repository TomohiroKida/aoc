import sys
import json
from enum import IntEnum
from functools import cmp_to_key
from mylibs.parse import parse_groups

def main():
  lines = open(sys.argv[1], "r").read().strip().split('\n')
  #for line in lines: print(line)
  print(solve1(lines))
  print(solve2(lines))

class State(IntEnum):
  CORRECT   = -1
  INCORRECT = 1 
  CONTINUE  = 0

def diff(left, right):
  #print(left, right)
  if type(left) is int and type(right) is int:
    if left < right: 
      return State.CORRECT
    elif left > right: 
      return State.INCORRECT 
    else:              
      return State.CONTINUE
  elif type(left) is list and type(right) is list:
    for x, l in enumerate(left):
      if len(right)-1 < x: 
        return State.INCORRECT
      ret = diff(l, right[x])
      #print(ret)
      if ret is not State.CONTINUE: 
        return ret
    if len(right)-1 > len(left)-1: 
      return State.CORRECT
  elif type(left) is int:
    ret = diff([left], right)
    if ret is not State.CONTINUE: 
      return ret
  else: #type(left) is list:
    ret = diff(left, [right])
    if ret is not State.CONTINUE: 
      return ret
  return State.CONTINUE


def solve1(lines):
  orders = []
  packets = parse_groups(lines)
  for pair_packet in packets:
    left, right = map(json.loads, pair_packet)
    print(left, 'vs', right)
    ret = diff(left, right)
    #print(ret)
    orders.append(ret)
  #print(orders)
  return (sum([i+1 for i, order in enumerate(orders) if order is State.CORRECT]))

def solve2(lines):
  orders = []
  packets = [json.loads(line) for line in lines if line != '']
  packets.append([[2]])
  packets.append([[6]])
  #print(packets)
  sorted_packets = sorted(packets, key=cmp_to_key(diff))
  #print(sorted_packets)
  div1 = sorted_packets.index([[2]])+1
  div2 = sorted_packets.index([[6]])+1
  return div1 * div2

if __name__ == "__main__":
    main()

import sys
import json
from enum import IntEnum
from functools import cmp_to_key, reduce
from operator import mul
from mylibs.parse import parse_groups

def main():
    lines = open(sys.argv[1], "r").read().strip().split('\n')
    for line in lines: print(line)
    print()
    print(solve1(lines))
    print(solve2(lines))

class State(IntEnum):
  CORRECT   = -1
  INCORRECT = 1 
  CONTINUE  = 0

def diff_int(left, right):
  if left < right: 
    return State.CORRECT
  elif left > right: 
    return State.INCORRECT 
  else:              
    return State.CONTINUE

def diff_list(left, right):
  for x, l in enumerate(left):
    if len(right)-1 < x: 
      return State.INCORRECT
    ret = diff(l, right[x])
    #print(ret)
    if ret is not State.CONTINUE: 
      return ret
  if len(right)-1 > len(left)-1: 
    return State.CORRECT
  else:
    return State.CONTINUE

def diff(left, right):
  #print(left, right)
  if (type(left) is int and
      type(right) is int):
    return diff_int(left, right)
  elif (type(left) is list and
        type(right) is list):
    return diff_list(left, right)
  elif type(left) is int:
    return diff_list([left], right)
  else: #type(left) is list:
    return diff_list(left, [right])

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
  divisors = [[[2]], [[6]]]
  packets += divisors
  #print(packets)
  sorted_packets = sorted(packets, key=cmp_to_key(diff))
  #print(sorted_packets)
  return reduce(mul, [sorted_packets.index(divisor)+1 for divisor in divisors])

if __name__ == "__main__":
    main()

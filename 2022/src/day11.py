import sys
from mylibs.parse import parse_groups
from functools import reduce

def main():
  lines = open(sys.argv[1], "r").read().strip().split('\n')
  for line in lines: print(line)
  groups = parse_groups(lines)
  print(solve1(groups))
  print(solve2(groups))

def genacc(op):
  if   op == '+': return lambda x, y: x + y
  elif op == '-': return lambda x, y: x - y
  elif op == '*': return lambda x, y: x * y
  elif op == '/': return lambda x, y: x / y
  elif op == '%': return lambda x, y: x % y
  else:           return lambda x, y: x
    
class Monkey:
  def __init__(self, group):
    self.num = (group[0].split(' ')[1][:-1])
    self.items = [int(x.strip()) for x in group[1].split(':')[1].split(',')]
    l, op, r = group[2].split('=')[1].lstrip().split(' ')
    self.acc = lambda n: genacc(op)(n if l=='old' else int(l), n if r=='old' else int(r))
    self.test = int(group[3].split(' ')[-1])
    self.t_value = int(group[4].split(' ')[-1])
    self.f_value = int(group[5].split(' ')[-1])
    self.cnt_inspect = 0

  def info(self):
    print(self.num, self.items)

  def turn(self, managerange):
    if len(self.items) == 0:
      return -1, -1
    self.cnt_inspect += 1
    wlv = self.items.pop(0) # worry level
    wlv = self.acc(wlv)
    wlv = managerange(wlv)
    if wlv % self.test == 0:
      return self.t_value, wlv
    else:
      return self.f_value, wlv

# divide by 3 to keep the number of worry level 
def one_round(monkeys):
  for monkey in monkeys:
    while True:
      to, wlv = monkey.turn(lambda n: int(genacc('/')(n, 3)))
      if (to, wlv) == (-1, -1):
        break
      monkeys[to].items.append(wlv)

# modulo by monkey test number to keep the number of worry level 
def one_round_first(monkeys, modulo):
  for monkey in monkeys:
    while True:
      to, wlv = monkey.turn(lambda n: int(genacc('%')(n, modulo)))
      if (to, wlv) == (-1, -1):
        break
      monkeys[to].items.append(wlv)

def solve1(groups):
  monkeys = [] 
  for group in groups: monkeys.append(Monkey(group))
  for x in range(20):
    one_round(monkeys)
  return reduce(lambda x, y: x*y, sorted([monkey.cnt_inspect for monkey in monkeys])[-2:])

def solve2(groups):
  monkeys = [] 
  for group in groups: monkeys.append(Monkey(group))
  modulo = reduce(lambda x, y: x*y, [monkey.test for monkey in monkeys])
  for x in range(10000):
    one_round_first(monkeys, modulo)
  return reduce(lambda x, y: x*y, sorted([monkey.cnt_inspect for monkey in monkeys])[-2:])

if __name__ == "__main__":
    main()

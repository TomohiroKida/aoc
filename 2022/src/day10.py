import sys

def main():
  lines = open(sys.argv[1], "r").read().strip().split('\n')
  for line in lines: print(line)
  print(solve1(lines))
  print(solve2(lines))

class STATE:
  FETCH = 0
  EXEC = 1

class CPU:
  def __init__(self, instructs):
    self.x = 1 
    self.pc = -1
    self.reg1 = None
    self.reg2 = None
    self.instructs = instructs
    self.state = STATE.FETCH

  def dump(self):
    print(self.x, self.pc, self.reg1, self.reg2, self.state) 

  def retx(self):
    return self.x

  def step(self):
    if self.state == STATE.FETCH:
      self.pc += 1
      if self.reg1 == 'addx':
        self.x += self.reg2
      if self.pc == len(self.instructs): 
        return False
      inst = self.instructs[self.pc]
      self.reg1 = inst[0]
      if self.reg1 == 'noop':
        return True 
      elif self.reg1 == 'addx':
        self.reg2 = int(inst[1])
        self.state = STATE.EXEC
        return True
    elif self.state == STATE.EXEC:
      self.state = STATE.FETCH
      return True

def solve1(lines):
  sig = 0
  instructs = [l.split(' ') for l in lines]
  cpu = CPU(instructs)
  clk = 0
  while True:
    clk += 1
    ret = cpu.step()
    if clk in [20, 60, 100, 140, 180, 220]:
      print(clk)
      cpu.dump()
      sig += cpu.retx() * clk
    if not ret:
      break
  return sig

def solve2(lines):
  pass

if __name__ == "__main__":
    main()

class Solver:
  def part1(self, file_path):
    elves = self.parse(file_path)
    print(max([sum(elf) for elf in elves]))

  def part2(self, file_path):
    elves = self.parse(file_path)
    print(sum(sorted([sum(elf) for elf in elves], reverse=True)[0:3]))

  def parse(self, file_path):
    with open(file_path, "r") as f:
      inputs = f.read()
      lines = inputs.strip().split("\n")
    elves = [[]]
    i = 0
    for line in lines:
      if line == "":
        elves.append([])
        i += 1
      else:
        elves[i].append(int(line))
    return elves
 

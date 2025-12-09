import re
"""
The safe has dial from 0 to 99 and start point is 50.
"""
class Solver:
  def part1(self, file_path):
    point = 50
    cnt = 0
    data:[[]] = self.parse(file_path)
    for direct, num in data:
      point += direct * num
      point %= 100
      if point == 0: cnt += 1
    return cnt

  def part2(self, file_path):
    point = 50
    cnt = 0
    data:[[]] = self.parse(file_path)
    for direct, num in data:
      prev = point
      print(direct, num, "====")
      print(cnt, point)
      point += direct * num

      # num of times turned dial
      laps = int(num / 100)
      point -= 100 * laps * direct
      cnt += laps
      if direct == 1: # Right
        if (point > 100 and 100 > prev): cnt += 1
      else: # Left
        if (point < 0 and 0 < prev): cnt += 1

      point %= 100
      if point == 0: cnt += 1
      print(cnt, point)
    return cnt

  def parse(self, file_path) -> [[]]:
    data = []
    lines = open(file_path, "r").read().strip().split("\n")
    for line in lines:
      assert re.match(r'L|R[0-9]+', line)
      # 'R' is 1, 'L' is -1
      direct = 1 if line[0] == 'R' else -1
      data.append([direct, int(line[1:])]) # [1 or -1, number]
    #print(data)
    return data

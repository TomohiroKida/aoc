import re


class Solver:
    def part1(self, file_path):
        games = self.parse(file_path)
        cnt = 0
        for game in games:
            head, sets = game.strip().split(":")
            time = int(head.strip().split(" ")[1])

            max_color = {"red": 0, "green": 0, "blue": 0}
            for cubes in sets.strip().split(";"):
                for cube in cubes.strip().split(","):
                    num, color = cube.strip().split(" ")
                    max_color[color] = max(max_color[color], int(num))
            if (max_color["red"] <= 12 and
                max_color["green"] <= 13 and 
                max_color["blue"] <= 14):
                cnt += time

        return cnt

    def part2(self, file_path):
        lines = self.parse(file_path)
        pass

    def parse(self, file_path):
        lines = open(file_path, "r").read().strip().split("\n")
        return lines

    def convert(self, line):
        return line

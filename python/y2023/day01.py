import re


class Solver:
    def part1(self, file_path):
        lines = self.parse(file_path)
        return sum(self.char2num(line) for line in lines)

    def part2(self, file_path):
        lines = self.parse(file_path)
        return sum(self.char2num(self.convert(l)) for l in lines)

    def parse(self, file_path):
        return open(file_path, "r").read().strip().split("\n")

    def char2num(self, line):
        ns = re.findall(r"\d", line)
        #print(ns)
        print(int(ns[0]+ns[-1]))
        return (int(ns[0]+ns[-1]))

    def convert(self, line):
        line = (
            line.replace("one", "one1one")
                .replace("two", "two2two")
                .replace("three", "three3three")
                .replace("four", "four4four")
                .replace("five", "five5five")
                .replace("six", "six6six")
                .replace("seven", "seven7seven")
                .replace("eight", "eight8eight")
                .replace("nine", "nine9nine")
        )
        return line

import sys
import os
import importlib


def main():
    print(sys.argv)
    if (len(sys.argv) < 4):
        print("$0 [year] [day] [part] [test]")
        exit()

    year = sys.argv[1]
    day = sys.argv[2]
    part = sys.argv[3]

    if len(sys.argv) == 4:
        file_path = "../data/{}/{}_input.txt".format(year, day)
    else:
        test = sys.argv[4]
        file_path = "../data/{}/{}_input_{}.txt".format(year, day, test)

    if not (os.path.isfile(file_path)):
        print("{} is no exist".format(file_path))
        exit()

    module = importlib.import_module("y{}.day{}".format(year, day))
    Solver = getattr(module, 'Solver')
    solver = Solver()
    if part == "2":
        print(solver.part2(file_path))
    else:
        print(solver.part1(file_path))

if __name__ == "__main__":
    main()

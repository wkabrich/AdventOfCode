
# AOC 2020 Day 1

from itertools import combinations


def main():
    part1()
    part2()


def part1():
    # our input is stored in ./input
    # open it and load it into a set
    with open("./input") as f:
        puzzleInput = [int(ln.strip()) for ln in f.readlines()]

    # comparison order does not matter
    # therefore as we proceed through the entries
    # remove each as we check against the remaining
    while len(puzzleInput) > 0:
        entry = puzzleInput.pop()

        for e in puzzleInput:
            if entry + e == 2020:
                print("Part 1:", entry * e)


def part2():
    # our input is stored in ./input
    # open it and load it into a set
    with open("./input") as f:
        puzzleInput = [int(ln.strip()) for ln in f.readlines()]

    # in part 2 I realize this is a combinatorics problem
    for i in list(combinations(puzzleInput, 3)):
        if i[0] + i[1] + i[2] == 2020:
            print("part 2:", i[0] * i[1] * i[2])


if __name__ == "__main__":
    main()

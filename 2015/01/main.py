
# AOC 2015 day 1

def main():
    rawInput = open("./input").readline()

    part1(rawInput)
    part2(rawInput)


def part1(instructions):
    floor = 0

    for step in instructions:
        if step == "(":
            floor += 1
        elif step == ")":
            floor -= 1

    print(floor)


def part2(instructions):
    floor = 0
    position = 0

    for step in instructions:
        if step == "(":
            floor += 1
        elif step == ")":
            floor -= 1

        position += 1

        if floor == -1:
            print(position)
            return


if __name__ == "__main__":
    main()

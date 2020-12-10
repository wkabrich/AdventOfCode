
# AoC 2015 Day 6

def main():
    with open("./input") as f:
        rawInput = [ln.strip() for ln in f.readlines()]

    structuredInput = []

    for i in rawInput:
        structuredInput.append(i.rsplit(' ', 3))

    part1(structuredInput)
    part2(structuredInput)


def part1(instructions):
    lit = 0
    grid = []

    for n in range(1000):
        grid.append(list(-1 for x in range(1000)))

    for instruction in instructions:
        for i in range(int(instruction[1].split(',')[0]), int(instruction[3].split(',')[0]) + 1):
            for j in range(int(instruction[1].split(',')[1]), int(instruction[3].split(',')[1]) + 1):
                if instruction[0] == 'toggle':
                    grid[i][j] *= -1
                elif instruction[0] == 'turn off':
                    grid[i][j] = -1
                elif instruction[0] == 'turn on':
                    grid[i][j] = 1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if int(grid[i][j]) > 0:
                lit += 1

    print(lit)


def part2(instructions):
    lit = 0
    grid = []

    for n in range(1000):
        grid.append(list(0 for x in range(1000)))

    for instruction in instructions:
        for i in range(int(instruction[1].split(',')[0]), int(instruction[3].split(',')[0]) + 1):
            for j in range(int(instruction[1].split(',')[1]), int(instruction[3].split(',')[1]) + 1):
                if instruction[0] == 'toggle':
                    grid[i][j] += 2
                elif instruction[0] == 'turn off':
                    grid[i][j] -= 1
                    if grid[i][j] < 0:
                        grid[i][j] = 0
                elif instruction[0] == 'turn on':
                    grid[i][j] += 1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            lit += grid[i][j]

    print(lit)


if __name__ == "__main__":
    main()

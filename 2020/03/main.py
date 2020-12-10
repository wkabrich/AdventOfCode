
# AoC 2020 Day 3

def main():
    with open("./input") as f:
        rawInput = [ln.strip() for ln in f.readlines()]

    part1(rawInput)
    part2(rawInput)


def part1(forest):
    print(traverse((3, 1), forest))


def part2(forest):
    answer = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for slope in slopes:
        answer *= traverse(slope, forest)

    print(answer)


def traverse(slope, forest):
    tree = '#'
    treesHit = 0
    xpos = 0

    for y in range(len(forest) // slope[1] - 1):
        ypos = y * slope[1] + slope[1]
        xpos += slope[0]

        # due to something you read about once involving arboreal genetics and biome stability,
        # the same pattern repeats to the right many times
        # if xpos runs off the edge, wrap around
        if xpos > len(forest[ypos]) - 1:
            xpos = xpos - len(forest[ypos])

        if forest[ypos][xpos] == tree:
            treesHit += 1

    return treesHit


if __name__ == "__main__":
    main()

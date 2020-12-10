
# AoC 2015 Day 2

def main():
    with open("./input") as f:
        rawInput = [ln.strip() for ln in f.readlines()]

    structuredInput = []

    for x in rawInput:
        structuredInput.append(x.split('x'))

    part1(structuredInput)
    part2(structuredInput)


def part1(prisms):
    totalPaper = 0

    for prism in prisms:
        l = int(prism[0])
        w = int(prism[1])
        h = int(prism[2])

        lw = l * w
        lh = l * h
        wh = w * h

        totalPaper += 2 * lw + 2 * lh + 2 * wh + min(lw, lh, wh)

    print(totalPaper)


def part2(prisms):
    totalRibbon = 0

    for prism in prisms:
        l = int(prism[0])
        w = int(prism[1])
        h = int(prism[2])

        plw = 2 * l + 2 * w
        plh = 2 * l + 2 * h
        pwh = 2 * w + 2 * h

        volume = l * w * h

        totalRibbon += min(plw, plh, pwh) + volume

    print(totalRibbon)


if __name__ == "__main__":
    main()

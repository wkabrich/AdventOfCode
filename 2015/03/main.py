
# AoC 2015 day 3

def main():
    rawInput = open("./input").readline()

    part1(rawInput)
    part2(rawInput)


def part1(moves):
    xpos = 0
    ypos = 0

    # He begins by delivering a present to the house at his starting location
    houses = {(0, 0): 1}

    for move in moves:
        if move == '^':
            ypos += 1
        elif move == '>':
            xpos += 1
        elif move == 'v':
            ypos -= 1
        elif move == '<':
            xpos -= 1

        house = (xpos, ypos)

        if house not in houses:
            houses[house] = 1
        else:
            houses[house] += 1

    print(len(houses))


def part2(moves):
    santaX = 0
    santaY = 0
    robotX = 0
    robotY = 0
    n = 1

    # Santa and Robo-Santa start at the same location (delivering two presents to the same starting house)
    houses = {(0, 0): 2}

    for move in moves:
        # if n is odd, move santa
        if n % 2:
            santaX, santaY = reposition(xpos=santaX, ypos=santaY, instruction=move)
            house = (santaX, santaY)
        # if n is even, move robot
        else:
            robotX, robotY = reposition(xpos=robotX, ypos=robotY, instruction=move)
            house = (robotX, robotY)

        if house not in houses:
            houses[house] = 1
        else:
            houses[house] += 1

        n += 1

    print(len(houses))


def reposition(xpos, ypos, instruction):
    if instruction == '^':
        ypos += 1
    elif instruction == '>':
        xpos += 1
    elif instruction == 'v':
        ypos -= 1
    elif instruction == '<':
        xpos -= 1

    return xpos, ypos


if __name__ == "__main__":
    main()

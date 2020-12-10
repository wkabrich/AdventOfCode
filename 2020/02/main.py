
# AOC 2020 Day 2

def main():
    with open("./input") as f:
        rawInput = [ln.strip() for ln in f.readlines()]

    structuredInput = []

    for row in rawInput:
        # normalize formatting so the characters between values are spaces
        row = row.replace('-', ' ').replace(':', '')

        # add the row to the list, splitting by space character
        structuredInput.append(row.split(' '))

    part1(structuredInput.copy())
    part2(structuredInput.copy())


def part1(validations):

    validPasswords = 0

    for row in validations:
        floor = int(row[0])
        ciel = int(row[1])
        char = row[2]

        if floor <= row[3].count(char) <= ciel:
            validPasswords += 1

    print(validPasswords)


def part2(validations):

    validPasswords = 0

    for row in validations:
        pos1 = int(row[0]) - 1
        pos2 = int(row[1]) - 1
        char = row[2]

        if row[3][pos1] == char and row[3][pos2] != char:
            validPasswords += 1
        elif row[3][pos1] != char and row[3][pos2] == char:
            validPasswords += 1

    print(validPasswords)


if __name__ == '__main__':
    main()


# AoC 2020 Day 7

def main():
    with open("./Input") as f:
        rawInput = f.read()

    structuredInput = rawInput.split('\n\n')

    groups = []

    for group in structuredInput:
        groups.append(group.split('\n'))

    part1(groups)
    part2(groups)


def part1(groups):
    count = 0

    for group in groups:
        answers = set()
        for questionnaire in group:
            for answer in questionnaire:
                answers.add(answer)

        count += len(answers)

    print(count)


def part2(groups):
    count = 0

    for group in groups:
        answers = set()
        for i in range(len(group)):
            if i == 0:
                answers = set(group[i])
            else:
                answers = answers & set(group[i])

        count += len(answers)

    print(count)


if __name__ == "__main__":
    main()

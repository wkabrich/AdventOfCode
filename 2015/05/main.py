
# AoC 2015 Day 5

def main():
    with open("./input") as f:
        rawInput = [ln.strip() for ln in f.readlines()]

    part1(rawInput)
    part2(rawInput)


def part1(strings):
    n = 0

    for word in strings:
        n += validate1(word)

    print(n)


def part2(strings):
    n = 0

    for word in strings:
        n += validate2(word)

    print(n)


def validate1(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    baddies = ['ab', 'cd', 'pq', 'xy']

    vowelsCount = 0
    doublesCount = 0

    for i in range(len(word)):
        sub = word[i:i+2]

        if vowels.count(word[i]):
            vowelsCount += 1

        if len(sub) > 1:
            if sub[0] == sub[1]:
                doublesCount += 1

        if baddies.count(sub):
            return 0

    if vowelsCount >= 3 and doublesCount >= 1:
        return 1
    else:
        return 0


def validate2(word):
    pairPairsCount = 0
    repeatWithGapCount = 0

    # find the pairs of pairs
    for i in range(len(word) - 1):
        isub = word[i:i + 2]
        remainingWord = word[i + 2:]

        for j in range(len(remainingWord) - 1):
            jsub = remainingWord[j:j + 2]

            if isub == jsub:
                pairPairsCount += 1

    # find the repeats with gaps
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            repeatWithGapCount += 1

    if pairPairsCount and repeatWithGapCount:
        return 1
    else:
        return 0


if __name__ == "__main__":
    main()

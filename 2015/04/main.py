
# AoC 2015 Day 4

import hashlib


def main():
    rawInput = open("./input").readline()

    part1(rawInput)
    part2(rawInput)


def part1(key):
    n = 0

    while 1:
        n += 1

        input = (key + str(n)).encode()

        hash = hashlib.md5(input)

        check = str(hash.hexdigest())[0:5]

        if check.count('0') == 5:
            print(n, hash.hexdigest())
            return


def part2(key):
    n = 0

    while 1:
        n += 1

        input = (key + str(n)).encode()

        hash = hashlib.md5(input)

        check = str(hash.hexdigest())[0:6]

        if check.count('0') == 6:
            print(n, hash.hexdigest())
            return


if __name__ == "__main__":
    main()

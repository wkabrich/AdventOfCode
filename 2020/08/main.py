
# AoC 2020 Day 8

from handheld import Handheld


def main():
    with open("./input") as f:
        rawInput = [ln.strip() for ln in f.readlines()]

    part1(rawInput)
    part2(rawInput)


def part1(instructions):
    gameboy = Handheld(instructions)
    seen = set()

    while (instructions[gameboy.index], gameboy.index) not in seen:
        seen.add((instructions[gameboy.index], gameboy.index))

        gameboy.processinstruction(instructions[gameboy.index].split(' '))

    print(gameboy.accumulator)


def part2(instructions):

    for i in range(len(instructions)):
        if instructions[i][:3] in ['jmp', 'nop']:
            newInstructions = instructions.copy()
            if newInstructions[i][:3] == 'jmp':
                newInstructions[i] = newInstructions[i].replace('jmp', 'nop')
            else:
                newInstructions[i] = newInstructions[i].replace('nop', 'jmp')

            cycle(newInstructions)


def cycle(instructions):
    gameboy = Handheld(instructions)
    seen = set()

    while (instructions[gameboy.index], gameboy.index) not in seen and gameboy.index < len(gameboy.instructions):
        seen.add((gameboy.instructions[gameboy.index], gameboy.index))

        gameboy.process()

        if gameboy.index >= len(gameboy.instructions):
            print(gameboy.instructions)
            print(gameboy.accumulator)
            return


if __name__ == "__main__":
    main()

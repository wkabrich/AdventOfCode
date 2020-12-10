
# AoC 2020 Day 7

import re


def main():
    with open("./Input") as f:
        rawInput = [ln.strip() for ln in f.readlines()]

    part1(rawInput)
    part2(rawInput)


class Bag:

    def __init__(self, texture, color):
        self.texture = texture
        self.color = color
        self.containedBags = []

    def contains(self, bag, quantity):
        self.containedBags.append(bag)


def part1(rules):
    print(findholders(rules, {'shiny gold'}))


def part2(rules):
    print(findheld(rules, 'shiny gold') - 1)


def findholders(rules, bags):
    found = set()

    for bag in bags:
        pattern = re.compile('^.*contain.*' + bag + '.*$')
        for rule in rules:
            if pattern.match(rule):
                found.add(rule[:rule.find(' bags contain')])

    if len(bags | found) == len(bags):
        return len(found)
    else:
        return findholders(rules, bags | found)


def findheld(rules, parent):
    pattern = re.compile('^' + parent + ' bags contain.*')
    bagRule = ''
    held = 1

    for rule in rules:
        if pattern.match(rule):
            bagRule = rule

    if not bagRule or 'contain no other bags' in bagRule:
        return held
    else:
        contents = bagRule[bagRule.find('bags contain ') + 13:]
        contents = contents.split(', ')

        for subBag in contents:
            quantity = subBag[:subBag.find(' ')]
            subBag = subBag[subBag.find(' ') + 1: subBag.find(' bag')]
            subBagHolds = int(quantity) * findheld(rules, subBag)

            held += subBagHolds

        return held


if __name__ == "__main__":
    main()

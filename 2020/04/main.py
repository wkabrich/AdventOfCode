
# AoC 2020 Day 4

import re


def main():
    rawInput = open("./input").read()

    # Passports are separated by blank lines.
    # separate the individual passports
    structuredInput = rawInput.split('\n\n')

    # remove newlines from within individual passports
    for i in range(len(structuredInput)):
        structuredInput[i] = structuredInput[i].replace('\n', ' ')

    # split each passport into a list of the fields
    for i in range(len(structuredInput)):
        structuredInput[i] = structuredInput[i].split(' ')

    # convert fields to tuples
    for i in range(len(structuredInput)):
        for j in range(len(structuredInput[i])):
            structuredInput[i][j] = tuple(structuredInput[i][j].split(':'))

    # convert the passport as list of tuples to a dict
    for i in range(len(structuredInput)):
        structuredInput[i] = dict(structuredInput[i])

    part1(structuredInput)
    part2(structuredInput)


def part1(passports):
    valid = 0

    for passport in passports:
        if validate_size(passport):
            valid += 1

    print(valid)


def part2(passports):
    valid = 0

    for passport in passports:
        if validate_size(passport) and validate_fields(passport):
            valid += 1

    print(valid)


def validate_size(passport):
    fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    }

    if fields.issubset(passport.keys()):
        return True
    else:
        return False


def validate_fields(passport):
    validFields = 0

    fieldValidationFunctions = {
        'byr': validate_byr,
        'iyr': validate_iyr,
        'eyr': validate_eyr,
        'hgt': validate_hgt,
        'hcl': validate_hcl,
        'ecl': validate_ecl,
        'pid': validate_pid,
        'cid': validate_cid
    }

    for field in passport:
        if fieldValidationFunctions.get(field)(passport[field]):
            validFields += 1

    if validFields == len(passport):
        return True
    else:
        return False


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
def validate_byr(byr):
    if 1920 <= int(byr) <= 2002:
        return True
    else:
        return False


# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
def validate_iyr(iyr):
    if 2010 <= int(iyr) <= 2020:
        return True
    else:
        return False


# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def validate_eyr(eyr):
    if 2020 <= int(eyr) <= 2030:
        return True
    else:
        return False


# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
def validate_hgt(hgt):
    value = hgt[:(len(hgt) - 2)]
    unit = hgt[(len(hgt) - 2):]

    if unit == 'in':
        if 59 <= int(value) <= 76:
            return True
    elif unit == 'cm':
        if 150 <= int(value) <= 193:
            return True
    else:
        return False


# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def validate_hcl(hcl):
    pattern = re.compile('^#[\\da-f]{6}$')

    if pattern.match(hcl):
        return True
    else:
        return False


# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def validate_ecl(ecl):
    validColors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

    if ecl in validColors:
        return True
    else:
        return False


# pid (Passport ID) - a nine-digit number, including leading zeroes.
def validate_pid(pid):
    pattern = re.compile('^\\d{9}$')

    if pattern.match(pid):
        return True
    else:
        return False


# cid (Country ID) - ignored, missing or not.
def validate_cid(cid):
    # we don't care if it's valid or not
    return True


if __name__ == "__main__":
    main()

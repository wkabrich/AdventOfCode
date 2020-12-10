
# AoC 2020 Day 5

def main():
    with open("./input") as f:
        rawInput = [ln.strip() for ln in f.readlines()]

    part1(rawInput)
    part2(rawInput)


def part1(tickets):
    highestID = 0

    for ticket in tickets:
        ticket = ticket.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1')
        ticketID = (int(ticket[:7], 2)) * 8 + (int(ticket[7:], 2))

        if ticketID > highestID:
            highestID = ticketID

    print(highestID)


def part2(tickets):
    seats = []

    for i in range(128):
        row = []
        for j in range(8):
            row.append(False)
        seats.append(row)

    for ticket in tickets:
        ticket = ticket.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1')
        seats[int(ticket[:7], 2)][int(ticket[7:], 2)] = True

    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if not seats[i][j]:
                if seats[i - 1][j] and seats[i + 1][j] and seats[i][j - 1] and seats[i][j + 1]:
                    print(i * 8 + j)


if __name__ == "__main__":
    main()

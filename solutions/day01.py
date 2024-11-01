def part1():
    total = 0
    with open("inputs/day01.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            digits = [x for x in line if x.isdigit()]
            total += int(digits[0] + digits[-1])
    print(f"Day 1, Part 1: {total}")


def part2():
    str_digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    total = 0
    with open("inputs/day01.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            digits = []
            for i, c in enumerate(line):
                if c.isdigit():
                    digits.append(c)
                else:
                    for ss, si in str_digits.items():
                        if line[i:].startswith(ss):
                            digits.append(str(si))
                        else:
                            pass
            total += int(digits[0] + digits[-1])
    print(f"Day 1, Part 2: {total}")


part1()
part2()

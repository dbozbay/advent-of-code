def part1():
    total_points = 0
    with open("inputs/day04.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            card_number, card = line.split(": ")
            card_number = int(card_number[5:])
            winning_numbers, card_numbers = card.split(" | ")
            winning_numbers = [int(num) for num in winning_numbers.strip().split()]
            card_numbers = [int(num) for num in card_numbers.strip().split()]
            matching_numbers = set(winning_numbers) & set(card_numbers)
            if len(matching_numbers) == 1:
                total_points += 1
            elif len(matching_numbers) > 1:
                total_points += 2 ** (len(matching_numbers) - 1)
            else:
                pass
    print(f"Day 04, Part 1: {total_points}")


def part2():
    with open("inputs/day04.txt", "r") as f:
        lines = f.readlines()
        line_index = 0
        while line_index < len(lines):
            line = lines[line_index]
            card_number, card = line.split(": ")
            card_number = int(card_number[5:])
            winning_numbers, card_numbers = card.split(" | ")
            winning_numbers = [int(num) for num in winning_numbers.strip().split()]
            card_numbers = [int(num) for num in card_numbers.strip().split()]
            matching_numbers = set(winning_numbers) & set(card_numbers)
            if len(matching_numbers) > 0:
                lines_to_copy = lines[
                    line_index + 1 : line_index + 1 + len(matching_numbers)
                ].copy()
                lines.extend(lines_to_copy)
            print(f"Line index complete: {line_index}")
            line_index += 1
    print(len(lines))
    for line in lines:
        print(line)


# part1()
part2()

import re


def part1() -> None:
    total = 0
    with open("inputs/day03.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        for line_idx, line in enumerate(lines):
            prev_line = lines[line_idx - 1] if line_idx - 1 >= 0 else None
            next_line = lines[line_idx + 1] if line_idx + 1 < len(lines) else None
            numbers = get_numbers_with_match(prev_line, line, next_line)
            for n in numbers:
                total += n
    print(f"Day 03, Part 1: {total}")


def get_numbers_with_match(
    prev_line: str | None,
    line: str,
    next_line: str | None,
) -> list[int]:
    numbers = []
    for match in re.finditer("[0-9]+", line):
        first_idx, last_idx = match.span()
        last_idx = last_idx - 1
        left_idx = first_idx - 1 if first_idx - 1 >= 0 else first_idx
        right_idx = last_idx + 1 if last_idx + 1 < len(line) else last_idx
        symbol_left = symbol_right = symbol_top = symbol_bottom = False
        symbol_left = first_idx - 1 >= 0 and line[first_idx - 1] != "."
        symbol_right = last_idx + 1 < len(line) and line[last_idx + 1] != "."
        if prev_line is not None:
            s = prev_line[left_idx : right_idx + 1]
            symbol_top = re.match("^[0-9.]+$", s) is None
        if next_line is not None:
            s = next_line[left_idx : right_idx + 1]
            symbol_bottom = re.match("^[0-9.]+$", s) is None
        if symbol_left or symbol_right or symbol_top or symbol_bottom:
            numbers.append(int(match.group()))
    return numbers


if __name__ == "__main__":
    part1()

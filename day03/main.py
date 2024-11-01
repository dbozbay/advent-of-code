def part1():
    total = 0
    symbols = ["*", "#", "+", "$"]
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f]
        for x, line in enumerate(lines):
            numbers = []
            current_number = ""
            for y in line:
                if y.isdigit():
                    current_number += y
                else:
                    if current_number:
                        numbers.append(current_number)
                        current_number = ""
            for number in numbers:
                x0 = x
                y0 = line.index(number)
                dy = len(number)
                xmin = max(x0 - 1, 0)
                xmax = min(x0 + 1, len(lines) - 1)
                ymin = max(y0 - 1, 0)
                ymax = min(y0 + dy, len(line) - 1)

                left = line[ymin] if ymin > 0 else None
                right = line[ymax] if ymax < len(line) - 1 else None
                top_row = lines[xmin][ymin : ymax + 1] if xmin > 0 else None
                bottom_row = (
                    lines[xmax][ymin : ymax + 1] if xmax < len(lines) - 1 else None
                )

                print("-" * 40)
                print("Number:", number)
                print("Left:", left)
                print("Right:", right)
                print("Top row:", top_row)
                print("Bottom row:", bottom_row)
                print("-" * 40)
    print("Day 3, Part 1:", total)


part1()

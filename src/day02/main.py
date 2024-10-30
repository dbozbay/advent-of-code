from math import prod


def part1():
    av = {"red": 12, "green": 13, "blue": 14}
    sum = 0
    with open("data.txt", "r") as f:
        lines = f.readlines()
        for idx, line in enumerate(lines):
            game_id = int(idx + 1)
            game_results = line.split(":")[1]
            game_sets = game_results.split(";")
            game_allowed = True
            for s in game_sets:
                set_results = s.split(",")
                for r in set_results:
                    count, color = r.strip().split(" ")
                    if av[color] < int(count):
                        game_allowed = False
            if game_allowed:
                sum += game_id
            else:
                pass
    print("Day 2, Part 1:", sum)


def part2():
    power = 0
    with open("data.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            results = line.split(":")[1]
            min_colors = {"red": 0, "blue": 0, "green": 0}
            for i, c in enumerate(results):
                for color, min_num in min_colors.items():
                    if results[i:].startswith(color):
                        count = int(
                            results[i - 3 : i - 1]
                            if results[i - 3].isdigit()
                            else results[i - 2]
                        )
                        if count > min_num:
                            min_colors[color] = count
                    else:
                        pass
            power += prod(min_colors.values())
    print("Day 2, Part 2:", power)


part1()
part2()

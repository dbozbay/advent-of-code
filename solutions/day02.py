def part1():
    MAX_COLORS = {"red": 12, "green": 13, "blue": 14}
    sum = 0
    with open("inputs/day02.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            game_is_allowed = True
            game_id, game_sets = line.strip().split(": ")
            game_id = int(game_id[5:])
            for game_set in game_sets.split("; "):
                for cubes_in_set in game_set.split(", "):
                    cube_count, cube_color = cubes_in_set.split(" ")
                    if int(cube_count) > MAX_COLORS[cube_color]:
                        game_is_allowed = False
            if game_is_allowed:
                sum += int(game_id)
    print("Day 2, Part 1:", sum)


def part2():
    total = 0
    with open("inputs/day02.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            _, game_sets = line.strip().split(": ")
            max_by_color = {"red": 0, "blue": 0, "green": 0}
            for game_set in game_sets.split("; "):
                for cubes_in_set in game_set.split(", "):
                    cube_count, cube_color = cubes_in_set.split(" ")
                    max_by_color[cube_color] = max(
                        max_by_color[cube_color], int(cube_count)
                    )
            power = max_by_color["red"] * max_by_color["green"] * max_by_color["blue"]
            total += power
    print("Day 2, Part 1:", total)


part1()
part2()

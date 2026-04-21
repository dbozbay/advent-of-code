def read_lines(filename: str) -> list[int]:
    with open(filename) as f:
        return [int(line.strip()) for line in f]


def count_increasing(numbers: list[int]) -> int:
    return sum(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))


def sums_of_threes(numbers: list[int]) -> list[int]:
     return [sum(numbers[i : i+3] for i in range


def count_increasing_window(numbers: list[int]) -> int:
    window_sum = 0
    current_window = []
    count = 0

    for i in range(len(numbers) - 1):
        if len(current_window) < 3:
            current_window.append(numbers[i])
        else:
            current_window_sum = sum(current_window)
            if current_window_sum > window_sum:
                count += 1
            window_sum = current_window_sum

    return count


if __name__ == "__main__":
    lines = read_lines("./input.txt")
    count = count_increasing_window(lines)
    print(count)

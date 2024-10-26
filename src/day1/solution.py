# Part 1:
# ------

total = 0

with open("data.txt", "r") as f:
    for line in f.readlines():
        digits = []
        for c in line:
            if c.isdigit():
                digits.append(c)
        if len(digits) > 1:
            n = int(digits[0] + digits[-1])
        else:
            n = int(digits[0] + digits[0])
        total += n

print("Total (neglecting worded digits): ", total)

# Part 2:
# ------

numbers = {
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


def has_integers(line: str) -> bool:
    return any(char.isdigit() for char in line)


def has_words(line: str, numbers=numbers) -> bool:
    return any(word in line for word in numbers)


def get_integers(line: str) -> list:
    return [i for i in line if i.isdigit()]


def get_words(line: str) -> list:
    return [w for w in numbers if w in line]


def get_min_index(line: str, num: str) -> int:
    return line.index(num)


def get_max_index(line: str, num: str) -> int:
    return line.rindex(num)


total = 0

with open("data.txt", "r") as f:
    for line in f.readlines():
        digits_list = []
        if has_integers(line):
            digits_list.append(get_integers(line))
        if has_words(line):
            digits_list.append(get_words(line))
        flat_digits_list = sum(digits_list, [])

        min_index_dict = {}
        max_index_dict = {}

        for digit in flat_digits_list:
            min_index_dict[digit] = get_min_index(line, digit)
            max_index_dict[digit] = get_max_index(line, digit)

        first_digit = min(min_index_dict, key=min_index_dict.get)
        last_digit = max(max_index_dict, key=max_index_dict.get)

        if not first_digit.isdigit():
            first_digit = str(numbers[first_digit])

        if not last_digit.isdigit():
            last_digit = str(numbers[last_digit])

        result = int(first_digit + last_digit)

        total += result

print("Total (counting worded digits)", total)

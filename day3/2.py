from pathlib import Path
import re

test_file = Path(__file__).parent / "./1_test.txt"
file = Path(__file__).parent / "./1.txt"


def calibrate(file_path):
    total = 0

    numbers = []
    symbols = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line_index, line in enumerate(lines):
            [symbols.append((line_index, found.start()))
             for found in re.finditer(r"[*]", line)]
            for found in re.finditer(r"[0-9]+", line):
                surrounding = []
                for i in range(found.start()-1, found.end()+1):
                    surrounding.append((line_index - 1, i))
                    surrounding.append((line_index, i))
                    surrounding.append((line_index + 1, i))
                numbers.append((surrounding, found.group()))

        for symbol in symbols:
            adjacent_numbers = []
            for number in numbers:
                if symbol in number[0]:
                    adjacent_numbers.append(int(number[1]))
            if len(adjacent_numbers) == 2:
                total += (adjacent_numbers[0]*adjacent_numbers[1])

    # print(numbers)
    # print(symbols)

    return total


print(f"Should be: 467835 \nIs: {calibrate(test_file)}")
print(calibrate(file))

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
             for found in re.finditer(r"[^0-9.\s]", line)]
            [numbers.append((line_index, found.start(), found.group()))
             for found in re.finditer(r"[0-9]+", line)]

        for number in numbers:
            found = False
            for l in range(-1, len(number[2])+1):
                if ((number[0]-1, number[1]+l) in symbols) or \
                    ((number[0], number[1]+l) in symbols) or \
                        ((number[0]+1, number[1]+l) in symbols):
                    found = True

            if found:
                total += int(number[2])

    print(numbers)
    print(symbols)

    return total


print(f"Should be: 4361 \nIs: {calibrate(test_file)}")
print(calibrate(file))

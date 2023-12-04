from pathlib import Path
import re

test_file = Path(__file__).parent / "./2_test"
file = Path(__file__).parent / "./1"

keys = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def calibrate(file_path):
    total = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            found = []
            for key in keys:
                if key in line:
                    for d in re.finditer(key, line):
                        found.append((keys[key], d.end()))

            for i in range(10):
                if str(i) in line:
                    for d in re.finditer(str(i), line):
                        found.append((str(i), d.end()))

            found.sort(key=lambda x: (x[1]))

            num = f"{found[0][0]}{found[-1][0]}"

            total += int(num)

    return total


print(f"Should be: 281 \nIs: {calibrate(test_file)}")
print(calibrate(file))

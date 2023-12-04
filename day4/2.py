from pathlib import Path
import re

test_file = Path(__file__).parent / "./1_test.txt"
file = Path(__file__).parent / "./1.txt"


def calibrate(file_path):
    total = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

        extra = [0] * len(lines)
        for index, line in enumerate(lines):
            winning = re.findall(r'\d+', line.split(":")
                                 [1].strip().split("|")[0])
            my_numbers = re.findall(
                r'\d+', line.split(":")[1].strip().split("|")[1])

            extras = 0
            for my in my_numbers:
                if my in winning:
                    extras += 1
                    extra[index + extras] += extra[index] + 1

            total += 1 + extra[index]

    return total


print(f"Should be: 30 \nIs: {calibrate(test_file)}")
print(calibrate(file))

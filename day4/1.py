from pathlib import Path
import re

test_file = Path(__file__).parent / "./1_test.txt"
file = Path(__file__).parent / "./1.txt"


def calibrate(file_path):
    total = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            winning = re.findall(r'\d+', line.split(":")
                                 [1].strip().split("|")[0])
            my_numbers = re.findall(
                r'\d+', line.split(":")[1].strip().split("|")[1])

            sub_total = 0
            for my in my_numbers:
                if my in winning:
                    if sub_total == 0:
                        sub_total = 1
                    else:
                        sub_total *= 2

            total += sub_total

    return total


print(f"Should be: 13 \nIs: {calibrate(test_file)}")
print(calibrate(file))

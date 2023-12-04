from pathlib import Path
import re

test_file = Path(__file__).parent / "./1_test"
file = Path(__file__).parent / "./1"


def calibrate(file_path):
    total = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            stripped = re.sub('[a-z]', '', line.strip())
            num = f"{stripped[0]}{stripped[-1]}"

            total += int(num)

    return total


print(f"Should be: 142 \nIs: {calibrate(test_file)}")
print(calibrate(file))

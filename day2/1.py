from pathlib import Path
import re

test_file = Path(__file__).parent / "./1_test"
file = Path(__file__).parent / "./1"

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def parse(line):
    id = re.search(r"\d+", line.split(":")[0]).group()

    possible = True
    for game in re.sub(r"Game \d+:", "", line).split(";"):
        if r := re.search(r"\d+ red", game):
            possible *= (int(re.search(r"\d+", r.group()).group())
                         <= limits["red"])
        if g := re.search(r"\d+ green", game):
            possible *= (int(re.search(r"\d+", g.group()).group())
                         <= limits["green"])
        if b := re.search(r"\d+ blue", game):
            possible *= (int(re.search(r"\d+", b.group()).group())
                         <= limits["blue"])

    return {
        "id": int(id),
        "possible": possible
    }


def calibrate(file_path):
    total = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            parsed_line = parse(line)

            if parsed_line["possible"]:
                total += parsed_line["id"]

    return total


print(f"Should be: 8 \nIs: {calibrate(test_file)}")
print(calibrate(file))

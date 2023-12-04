from pathlib import Path
import re

test_file = Path(__file__).parent / "./2_test"
file = Path(__file__).parent / "./1"


def parse(line):
    id = re.search(r"\d+", line.split(":")[0]).group()

    red, green, blue = 0, 0, 0
    for game in re.sub(r"Game \d+:", "", line).split(";"):
        if r := re.search(r"\d+ red", game):
            new_red = int(re.search(r"\d+", r.group()).group())
            red = new_red if new_red > red else red
        if g := re.search(r"\d+ green", game):
            new_green = int(re.search(r"\d+", g.group()).group())
            green = new_green if new_green > green else green
        if b := re.search(r"\d+ blue", game):
            new_blue = int(re.search(r"\d+", b.group()).group())
            blue = new_blue if new_blue > blue else blue

    return {
        "id": int(id),
        "red": red,
        "green": green,
        "blue": blue
    }


def calibrate(file_path):
    total = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            parsed_line = parse(line)
            print(parsed_line)
            total += parsed_line["red"] * parsed_line["green"] * parsed_line["blue"]

    return total


print(f"Should be: 2286 \nIs: {calibrate(test_file)}")
print(calibrate(file))

from dataclasses import dataclass

max_cubes = {"red": 12, "green": 13, "blue": 14}


@dataclass
class Round:
    red: int = 0
    blue: int = 0
    green: int = 0


def parse_round_string(round_str):
    round_obj = Round()

    for part in round_str.split(","):
        quantity, color = part.strip().split()
        setattr(round_obj, color.lower(), int(quantity))

    return round_obj


# part 1
result = 0

with open("data.txt") as data_file:
    for i, line in enumerate(data_file):
        cleaned_string = line.split(":", 1)[1].strip()
        games = [
            parse_round_string(round_str) for round_str in cleaned_string.split(";")
        ]

        invalid_rounds = any(
            round.green > max_cubes["green"]
            or round.red > max_cubes["red"]
            or round.blue > max_cubes["blue"]
            for round in games
        )

        if not invalid_rounds:
            result += i + 1

print(f"Result part 1: {result}")

# part 2
result = 0

with open("data.txt") as data_file:
    for i, line in enumerate(data_file):
        cleaned_string = line.split(":", 1)[1].strip()
        games = [
            parse_round_string(round_str) for round_str in cleaned_string.split(";")
        ]

        green = 0
        red = 0
        blue = 0

        for round in games:
            green = max(green, round.green)
            blue = max(blue, round.blue)
            red = max(red, round.red)

        result += green * blue * red


print(f"Result part 2: {result}")

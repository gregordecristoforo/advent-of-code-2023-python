lines = open("data.txt", "r").read().splitlines()


def extract_numbers_part_1(line):
    _, values = line.split(": ")
    values = values.split(" ")
    while "" in values:
        values.remove("")
    return values


def extract_numbers_part_2(line):
    _, values = line.split(": ")
    values = values.replace(" ", "")
    return values


def calculate_races(times, distances):
    result = 1
    for time, distance in zip(times, distances):
        beating_record = 0
        for i in range(1, int(time)):
            if i * (int(time) - i) > int(distance):
                beating_record += 1
        result *= beating_record
    return result


times = extract_numbers_part_1(lines[0])
distances = extract_numbers_part_1(lines[1])
result = calculate_races(times, distances)
print(f"Result part 1: {result}")

times = extract_numbers_part_2(lines[0])
distances = extract_numbers_part_2(lines[1])
result = calculate_races([times], [distances])
print(f"Result part 2: {result}")

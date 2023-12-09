from itertools import cycle

lines = open("data.txt", "r").read().splitlines()

left_or_right = lines[0]

directions = {}
for line in lines[2:]:
    name, direction = line.split(" = ")
    direction = direction.replace("(", "").replace(")", "")
    left, right = direction.split(", ")
    directions[name] = (left, right)


steps = 0
position = "AAA"
# while position != "ZZZ":
for direction in cycle(left_or_right):
    if position == "ZZZ":
        break
    if direction == "L":
        position = directions[position][0]
    elif direction == "R":
        position = directions[position][1]
    else:
        raise ValueError("Directions must be wrong")

    steps += 1

print(f"Solution part 1: {steps}")


lines = open("test_data_part_2.txt", "r").read().splitlines()

left_or_right = lines[0]

directions = {}
for line in lines[2:]:
    name, direction = line.split(" = ")
    direction = direction.replace("(", "").replace(")", "")
    left, right = direction.split(", ")
    directions[name] = (left, right)


starts = [position for position in directions if position[2] == "A"]
steps = 0
all_at_the_end = False
for direction in cycle(left_or_right):
    if all_at_the_end:
        break
    steps += 1
    all_at_the_end = True
    # print(starts)
    for i in range(len(starts)):
        start = starts[i]
        if direction == "L":
            start = directions[start][0]
        elif direction == "R":
            start = directions[start][1]
        else:
            raise ValueError("Directions must be wrong")
        starts[i] = start
        if start[-1] != "Z":
            all_at_the_end = False

print(steps)

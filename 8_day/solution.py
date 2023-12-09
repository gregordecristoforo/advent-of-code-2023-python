def circular_string_generator(input_string):
    index = 0
    length = len(input_string)
    while True:
        if length > 0:
            yield input_string[index]
            index = (index + 1) % length
        else:
            raise StopIteration


lines = open("data.txt", "r").read().splitlines()

left_or_right = lines[0]

directions = {}
for line in lines[2:]:
    name, direction = line.split(" = ")
    direction = direction.replace("(", "").replace(")", "")
    left, right = direction.split(", ")
    directions[name] = (left, right)


circular_iterator = circular_string_generator(left_or_right)

steps = 0
position = "AAA"
while position != "ZZZ":
    direction = next(circular_iterator)
    if direction == "L":
        position = directions[position][0]
    elif direction == "R":
        position = directions[position][1]
    else:
        raise ValueError('Directions must be wrong')

    steps += 1

print(steps)

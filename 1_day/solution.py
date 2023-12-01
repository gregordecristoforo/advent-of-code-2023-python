# Part 1
data_file = open("data.txt")

result = 0
for row in data_file:
    digits_only = "".join([char for char in row if char.isdigit()])
    two_digit = int(digits_only[0] + digits_only[-1])
    result += two_digit

print(f"Result is {result}")


# Part 2
data_file = open("data.txt")

word_to_number = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def calculate_calibration_value(line: str):
    numbers = []

    for index in range(len(line)):
        if line[index].isdigit():
            numbers.append(line[index])
        else:
            # check if this is the beginning of a number string
            for number_string in word_to_number:
                if line[index:].startswith(number_string):
                    numbers.append(word_to_number[number_string])

    return int(numbers[0] + numbers[-1])


result = 0
for row in data_file:
    result += calculate_calibration_value(row)

print(f"Result is {result}")

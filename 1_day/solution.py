data_file = open("data.txt")

result = 0
for row in data_file:
    digits_only = ''.join([char for char in row if char.isdigit()])
    two_digit = int(digits_only[0] + digits_only[-1])
    result += two_digit

print(f"Result is {result}")

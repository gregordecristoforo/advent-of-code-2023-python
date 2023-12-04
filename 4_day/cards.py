def get_points_per_card(card):
    card = card.replace("\n", "")
    _, numbers = card.split(": ")
    winning_numbers, your_numbers = numbers.split(" | ")
    winning_numbers = set(winning_numbers.split(" "))
    your_numbers = set(your_numbers.split(" "))
    winning_numbers.discard("")
    your_numbers.discard("")
    return len(winning_numbers.intersection(your_numbers))


# part 1
with open("data.txt") as data_file:
    result = 0
    for card in data_file:
        matching_cards = get_points_per_card(card)
        if matching_cards:
            result += 2 ** (matching_cards - 1)
    print(f"result part 1: {result}")

# part 2
with open("data.txt") as data_file:
    number_of_cards = [1] * 199
    for i, card in enumerate(data_file):
        matching_cards = get_points_per_card(card)
        for j in range(i + 1, i + 1 + matching_cards):
            number_of_cards[j] += number_of_cards[i]
    print(f"result part 2: {(sum(number_of_cards))}")

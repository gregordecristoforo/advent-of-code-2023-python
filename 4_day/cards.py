# part 1
with open("data.txt") as data_file:
    result = 0
    for card in data_file:
        print(card)
        card = card.replace("\n", "")
        _, numbers = card.split(": ")
        winning_numbers, your_numbers = numbers.split(" | ")
        winning_numbers = set(winning_numbers.split(" "))
        your_numbers = set(your_numbers.split(" "))
        winning_numbers.discard("")
        your_numbers.discard("")
        matching_cards = len(winning_numbers.intersection(your_numbers))
        if matching_cards:
            result += 2**(matching_cards-1)
    print(f"result part 1: {result}")

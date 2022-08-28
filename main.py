import random
from replit import clear

def inital_cards():
    """ Prepares all cards"""
    symbols = ["red diamonds", "black clubs", "red hearts", "black spades"]
    for s in symbols:
        for n in range(1, 14):
            total_cards.append(s + " " + str(n))
    return total_cards

def deal_card():
    """ Returns a card """
    card = random.choice(total_cards)
    total_cards.remove(card)
    return card

def calculate_score(cards):
    # 1(A) can be 1 or 11 scores, 10-13 are 10 scores, others are their original number scores
    """ Calculate the score of cards """
    temp_cards = []
    total = 0
    number_of_ace = 0

    # get the number part of a card
    for card in cards:
        temp_cards.append(int(card.split(" ")[2]))

    # sum up numbers except A
    for num in temp_cards:
        if num == 1:
            number_of_ace += 1
        else:
            if num > 10:
                total += 10
            else:
                total += num
    # deal with A
    while number_of_ace > 0:
        if total <= 10:
            total += 11
        else:
            total += 1
        number_of_ace -= 1
    return total

total_cards = []
user_cards = []
computer_cards = []
inital_cards()
is_game_over = False

for _ in range (1, 3):
    user_cards.append(deal_card())

for _ in range (1, 3):
    computer_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    # print(f"Computer cards: {computer_cards}, current score: {computer_score}")

    if user_score == 21 or computer_score == 21 or user_score > 21:
        is_game_over = True
        if user_score == 21:
            print("You win! Black Jack")
        elif computer_score == 21:
            print("You lose! Bust")
        else:
            print("You lose!")
    else:
        user_decision = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_decision == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True


while computer_score < user_score and computer_score < 16:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print()
if user_score < 21:
    if computer_score > 21:
        print("You win")
    else:
        if user_score == computer_score:
            print("Draw")
        elif user_score > computer_score:
            print("You win!")
        else:
            print("You lose")

print(f"Your cards: {user_cards}, final score: {user_score}")
print(f"Computer cards: {computer_cards}, final score: {computer_score}")

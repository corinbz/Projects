import random

deck = [n for n in range(0, 52)]
random.shuffle(deck)

def name(card_idx):
    # Card indices are numbered 0 - 51. Every fourteenth card is a new suit
    suits = ["diamonds", "hearts", "clubs", "spades"]
    cards = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
             "jack", "queen", "king"]
    isuit = card_idx // 13
    icard = card_idx % 13
    txt = cards[icard] + " of " + suits[isuit]
    return txt

def value(card_idx):
    val = card_idx % 13 + 1 if card_idx % 13 < 10 else 10  # your code to determine the card value from its index
    return val # Value is a number between 1 and 10

def total(hand):
    tot = sum([value(c) for c in hand])
    if tot + 10 <= 21:
        tot += 10
    # Iterate over the cards in hand, and calculate the total value.
    return tot # Additional question: What happens if you use the variable name ↪"value" instead of "tot" here?


def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def player():
    score = 0
    playing = True
    while playing:
        card = draw_card(deck)
        score += value(card)
        print(f" Your score is now {score}.")
        if score > 21:
            print(f"You lost! Your hand is {score}.")
            break
        elif score == 21:
            print("Blackjack!")
            break
        else:
            draw_another = input("Would you like to draw another? Y/N \n")
            if draw_another.lower() == "y":
                continue
            else:
                print(f"Your final score is {score}.")
                break
    return score

player()
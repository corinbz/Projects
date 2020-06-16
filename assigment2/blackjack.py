import random
import numpy as np

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
    global result
    cards = []
    card = draw_card(deck)
    cards.append(value(card))
    while True:
        card = draw_card(deck)
        cards.append(value(card))
        score = sum(cards)
        alt_score = sum(cards) + 10 if 1 in cards and sum(cards) + 10 < 22 else 0
        # print(cards)
        print(f"Your hand is now {score}/{alt_score}." if alt_score else f"Your hand is {score}.")
        for c in cards:
            print(name(c-1))
        if score > 21:
            print(f"You busted! Your hand is {score}.")
            result.append(f"{name_players[n-1]} vs Bank! \n You lost!\n")
            break
        elif score == 21:
            print("Blackjack!")
            break
        else:
            draw_another = input("Would you like to draw another? Y/N \n")
            if draw_another.lower() == "y":
                continue
            else:
                print(f"Your final hand is {score}.")
                break
    return score



def bank(scores):
    global score
    global card
    global name_players
    global result
    running = True

    while running:
        card = draw_card(deck)
        score += value(card)
        # print(f"Bank hand is {score}.")
        if score > 21:
            print("Bank busted!")
            for player_score in scores:
                if player_score < 22:
                    result.append(f"{name_players[scores.index(player_score)]} vs Bank!\n You won!\n")
            running = False

        elif score < 17:
            continue
        if 16 < score < 22:
            for player_score in scores:
                if score > player_score:
                    result.append(f"{name_players[scores.index(player_score)]} vs Bank!\n You lost!\n")
                    continue
                elif score == player_score:
                    result.append(f"{name_players[scores.index(player_score)]} vs Bank!\nIt's a draw!\n")
                    continue
                elif  score < player_score < 22:
                    result.append(f"{name_players[scores.index(player_score)]} vs Bank!\n You won!\n")
                    continue
            running = False
    print(f"\nBank's hand is {score}.\n")
    for i in result:
        print(i)



result = []

card = draw_card(deck)
score = value(card)
first_bank_c = (f"Bank has a {name(card)} ({value(card)}).")

nr_players = input("How many players?")
name_players = []
for n in range(int(nr_players)):
    name_players.append(input(f"Player {n+1} name: "))

def play():
    global first_bank_c
    player_chips = np.full(int(nr_players), 100)
    players_scores = []
    print(first_bank_c)
    for n in range(int(nr_players)):
        print(f"\n{name_players[n]}'s turn! \n")
        players_scores.append(player())
    bank(players_scores)

play()
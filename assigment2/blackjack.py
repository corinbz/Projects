import random
import numpy as np

deck = [n for n in range(0, 416)]
random.shuffle(deck)

def name(card_idx):
    # Card indices are numbered 0 - 51. Every fourteenth card is a new suit
    suits = ["diamonds", "hearts", "clubs", "spades"]
    cards = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
             "jack", "queen", "king"]
    isuit = card_idx // 13 if card_idx // 13 < 4 else card_idx // 13 % 4
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
    """Draws a card and removes it from the deck"""
    card = random.choice(deck)
    deck.remove(card)
    return card

def player(player):
    """Function for playing the hand that returns the total score"""
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
            result.append(f"{name_players[player]} vs Bank! \n You lost!\n")
            break
        elif score == 21:
            print("Blackjack!")
            break
        else:
            while True:
                draw_another = input("Would you like to draw another card? Y/N \n")
                if draw_another.lower() in ["y", "n", "yes", "no"] and len(draw_another) < 4:
                    break
                else:
                     print("Please enter yes/y or no/n !")
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
        #Draws the second card and adds it's value to the score
        card = draw_card(deck)
        bank_cards.append(card)
        score = total(bank_cards)
        #When total hand is higher than 21 stop the loop
        if score > 21:
            print("Bank busted!")
            #if players are not busted, store the result
            for player_score in scores:
                if player_score < 22:
                    result.append(f"{name_players[scores.index(player_score)]} vs Bank!\nYou won!\n")
            running = False

        if 17 < score < 22 :
            #bank stops drawing , compares the scores and stores the result
            for player_score in scores:
                if score > player_score:
                    result.append(f"{name_players[scores.index(player_score)]} vs Bank!\nYou lost!\n")
                    continue
                elif score == player_score:
                    result.append(f"{name_players[scores.index(player_score)]} vs Bank!\nIt's a draw!\n")
                    continue
                elif  score < player_score < 22:
                    result.append(f"{name_players[scores.index(player_score)]} vs Bank!\nYou won!\n")
                    continue
        elif score == 17 and 1 in [value(c) for c in bank_cards]:
            continue
        else:
            continue
        running = False

    #Prints the final result
    print(f"\nBank's hand is {score}.\n")
    for i in result:
        print(i)

def play():
    global first_bank_c
    # player_chips = np.full(int(nr_players), 100)
    players_scores = []
    print(first_bank_c) #Prints bank's first card

    #Each player plays his hand and add the result to player scroes
    for n in range(int(nr_players)):
        print(f"\n{name_players[n]}'s turn! \n")
        players_scores.append(player(n))

    bank(players_scores)

result = [] #Stores strings about result between player and bank

########### Draws a card for the bank and stores it to be printed later #######
card = draw_card(deck)
bank_cards = []
bank_cards.append(0)
score = total(bank_cards)  #The bank's total score
first_bank_c = (f"Bank has a {name(card)} ({value(card)}).")

########## Get the info about players ###########
while True:
    nr_players = input("How many players?\n")
    if nr_players.isdigit() == True and 0 < int(nr_players) <= 7:
        break
    else:
         print("Please enter a number between 1 and 7!\n")

name_players = []
for n in range(int(nr_players)):
    name_players.append(input(f"Player {n+1} name: "))




play()

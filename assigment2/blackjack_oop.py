import random


# import numpy as np


class Deck:
    """Contains the deck of cards"""

    def __init__(self):
        self.ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                      "jack", "queen", "king"]
        self.suits = ["diamonds", "hearts", "clubs", "spades"]
        self.deck = list(range(52))

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self, cards=1):
        cards_drawed = []
        for _ in range(cards):
            cards_drawed.append(self.deck.pop())
        return cards_drawed


class Card(Deck):

    def __init__(self, index):
        super().__init__()
        self.rank = self.ranks[index % 13]
        self.suit = self.suits[index // 13]
        self.index = index
        self.card_value = self.index % 13 + 1 if self.index % 13 < 10 else 10

    def __str__(self):
        return str(self.rank) + " of " + str(self.suit)


class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.hand_value = sum([Card(c).card_value for c in hand])
        if 1 in [Card(c).card_value for c in hand] and sum([Card(c).card_value for c in hand]) + 10 < 22:
            self.hand_value_alt = sum([Card(c).card_value for c in hand]) + 10
        else:
            self.hand_value_alt = 0

    def display(self):
        display_cards = ""
        for c in self.hand:
            display_cards += str(Card(c)) + "\n"
        return display_cards

    def display_one(self):
        return Card(self.hand[0])

# class Day(object):
#     …
#     def __add__(self, other):
#         total_visits = self.visits + other.visits
#         total_contacts = self.contacts + other.contacts
#         return Day(total_visits, total_contacts)
    def __add__(self, other):
        self.hand.append(other)
        return Hand(self.hand)




class Game:

    def __init__(self):
        self.nr_players = 1
        self.name_players = ['corin']
        self.deck = Deck()
        self.deck.shuffle()
        # Deal each player 2 cards
        self.dealer_hand = Hand(self.deck.draw(2))
        # self.players_hands =[Hand(self.deck.draw(2)) for _ in range(self.nr_players)]
        # Show one card from the dealer
        print(f"Dealer has a {self.dealer_hand.display_one()}.")

    def play(self):
        players_hands =[Hand(self.deck.draw(2)) for _ in range(self.nr_players)]
        for player in range(self.nr_players):
            print(f"{self.name_players[player]}'s turn!")
            playing = True
            # Ask if you want to draw another
            while playing:
                if players_hands[player].hand_value_alt != 0:
                        print(f"Your hand is now {players_hands[player].hand_value}/{players_hands[player].hand_value_alt}: \n{players_hands[player].display()}")
                else:
                    print(f"Your hand is now {players_hands[player].hand_value}: \n{players_hands[player].display()}")

                while True:
                    draw_another = input("Would you like to draw another card? Y/N \n")
                    if draw_another.lower() in ["y", "n", "yes", "no"] and len(draw_another) < 4:
                        break
                    print("Please enter yes/y or no/n !")
                if draw_another.lower() == "y" or draw_another.lower() == "yes":
                    players_hands[player] += int(self.deck.draw()[0])
                    continue
                else:
                    print(f"Your final hand is {players_hands[player].hand_value}.")
                    playing = False

# Needed variables : Deck, player scores, nr_players, name_players
# Ask for user input
#TODO easier to debug
# while True:
#     nr_players = input("How many players?\n")
#     if nr_players.isdigit() == True and 0 < int(nr_players) <= 7:
#         break
#     else:
#         print("Please enter a number between 1 and 7!\n")
#
# name_players = []
# for n in range(int(nr_players)):
#     name_players.append(input(f"Player {n + 1} name: "))




game = Game()
game.play()

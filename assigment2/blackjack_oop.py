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

    def draw(self):
        return self.deck.pop(0)


class Card(Deck):

    def __init__(self, index):
        super().__init__()
        self.rank = self.ranks[index % 13]
        self.suit = self.suits[index // 13]
        self.index = index

    def __str__(self):
        return str(self.rank) + " of " + str(self.suit)


class Hand:
    def __init__(self, hand):
        self.hand = hand
        self. = [index % 13 + 1 if index % 13 < 10 else 10

    def display(self):
        for c in self.hand:
            print(c)
class Game:

    def __init__(self):
        pass


class Play:
    pass


d = Hand([0, 2])
print(d.hand_value)
# d.shuffle()
# print(d.deck)
import random


class Deck:
    """Contains the deck of cards"""

    def __init__(self):
        """ Defines the ranks, suits and deck."""
        self.ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                      "jack", "queen", "king"]
        self.suits = ["diamonds", "hearts", "clubs", "spades"]
        self.deck = list(range(52))

    def shuffle(self):
        """ Shuffles the deck."""
        random.shuffle(self.deck)

    def draw(self, cards=1):
        """ Returns a card(if no value is passed) and deletes it from the deck."""
        return [self.deck.pop() for _ in range(cards)]


class Card(Deck):
    """Card class child of Deck. It has it's own rank, suit, index, value"""
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
        self.hand_value = sum(Card(c).card_value for c in hand)

        # Check if A is in the hand, and add it to total hand alternative
        if (
            1 in [Card(c).card_value for c in hand]
            and sum([Card(c).card_value for c in hand]) < 12
        ):
            self.hand_value_alt = sum(Card(c).card_value for c in hand) + 10
        else:
            self.hand_value_alt = 0

    def display(self):
        display_cards = ""
        for c in self.hand:
            display_cards += str(Card(c)) + "\n"
        return display_cards

    def display_one(self):
        return str(Card(self.hand[0]))

    def get_score(self):
        if self.hand_value_alt != 0:
            print(
                f"Your hand value is now {self.hand_value}/{self.hand_value_alt}: \n{self.display()}")
        else:
            print(f"Your hand value is now {self.hand_value}: \n{self.display()}")

    def has_ace(self):
        return 1 in [int(Card(c).card_value) for c in self.hand]

    def __add__(self, other):
        self.hand.append(other)
        return Hand(self.hand)


class Game:

    def __init__(self):

        # Get the number of players / name of players
        while True:
            self.nr_players = input("How many players?\n")
            if self.nr_players.isdigit() == True and 0 < int(self.nr_players) <= 7:
                self.nr_players = int(self.nr_players)
                break
            else:
                print("Please enter a number between 1 and 7!\n")

        self.name_players = []
        for n in range(self.nr_players):
            self.name_players.append(input(f"Player {n + 1} name: "))
        self.bet = int()
        self.dealer_hand = []
        self.chips = [100] * self.nr_players
        self.player_hand = Hand

    @staticmethod
    def ask_to_draw():
        # Ask if you want to draw another
        while True:
            draw_another = input("Would you like to draw another card? Y/N \n")
            if draw_another.lower() in ["y", "n", "yes", "no"] and len(draw_another) < 4:
                break
            print("Please enter yes/y or no/n !")
        if draw_another.lower() in ["y", "yes"]:
            return 1
        else:
            return 0

    def players_loop(self, player):
        self.make_bet(player)
        self.player_hand = Hand(self.deck.draw(2))
        self.player_hand.get_score()
        while True:
            if self.player_hand.hand_value > 21:
                print(f"Your final hand value is {self.player_hand.hand_value}.")
                break
            if Game.ask_to_draw():
                self.player_hand += int(self.deck.draw()[0])
                self.player_hand.get_score()
                continue
            else:
                if self.player_hand.hand_value_alt < self.player_hand.hand_value:
                    print(f"Your final hand value is {self.player_hand.hand_value}.")
                else:
                    print(f"Your final hand value is {self.player_hand.hand_value_alt}.")
                break

    def dealers_loop(self):
        self.dealer_hand = Hand(self.deck.draw(2))
        print(f"Dealer has a(n) {self.dealer_hand.display_one()}.")
        while True:
            if self.dealer_hand.hand_value > 21:
                # print(f"Dealer busted with {self.dealer_hand.hand_value}!")
                break
            elif self.dealer_hand.hand_value == 17 and not self.dealer_hand.has_ace():
                # print(f"Dealer's total hand is {self.dealer_hand.hand_value}")
                break
            elif 17 < self.dealer_hand.hand_value < 22 or 17 < self.dealer_hand.hand_value_alt < 22:
                # print(f"Dealer's total hand is"
                #       f" {max([self.dealer_hand.hand_value, self.dealer_hand.hand_value_eleven])}")
                break
            else:
                self.dealer_hand += int(self.deck.draw()[0])
                continue

    # TODO split the hand function
    # def split_the_hand(self, player):
    #     self.players_hands[player].get_score()
    #     if Card(self.players_hands[player].hand[0]).card_value == Card(self.players_hands[player].hand[1]).card_value:
    #         if input("Would you like to split the hand? Y/N").lower() == "y":
    #             self.players_hands[player].hand[player:player] = self.players_hands[player].hand[player][0]
    #             self.players_hands[player].hand[player+1:player+1] = self.players_hands[player].hand[player][1]
    #             # self.players_hands[player][0] = self.players_hands[player].hand[0]
    #             # self.players_hands[player][1] = self.players_hands[player].hand[1]

    def get_results(self, player):
        if self.player_hand.hand_value > 21:
            print(f"Sorry {self.name_players[player]}, you lost!")
            self.chips[player] -= self.bet
        elif self.dealer_hand.hand_value > 21:
            print(f"Congratulations {self.name_players[player]}! You won!")
            self.chips[player] += self.bet
        elif self.dealer_hand.hand_value < self.player_hand.hand_value < 22:
            print(f"Congratulations {self.name_players[player]}! You won!")
            self.chips[player] += self.bet
        elif self.dealer_hand.hand_value < self.player_hand.hand_value_alt < 22:
            print(f"Congratulations {self.name_players[player]}! You won!")
            self.chips[player] += self.bet
        elif self.dealer_hand.hand_value == self.player_hand.hand_value:
            print("It's a draw!")
        elif self.dealer_hand.hand_value_alt == self.player_hand.hand_value:
            print("It's a draw!")
        else:
            print(f"Sorry {self.name_players[player]}, you lost!")
            self.chips[player] -= self.bet

    def make_bet(self, player):
        while True:
            self.bet = input(f"You have {self.chips[player]} chips.\nPlease insert how much you would like to bet:\n")
            if self.bet.isnumeric():
                if self.chips[player] < int(self.bet) or int(self.bet) < 0:
                    print(f"Number is out of range! Enter a number between 1 and {self.chips[player]} !")
                    continue
            elif not self.bet.isnumeric():
                print("Please insert a valid numeric value!")
                continue
            break
        self.bet = int(self.bet)

    def play(self):
        while True:
            self.deck = Deck()
            self.deck.shuffle()
            for player in range(self.nr_players):
                self.dealers_loop()
                print(f"\n{self.name_players[player]}'s turn!")
                self.players_loop(player)
                self.get_results(player)
                print(f"You have now {self.chips[player]} chips.\n")
            if input("Would you like to play again? Y/N\n").lower() in ["y", "yes"]:
                continue
            break


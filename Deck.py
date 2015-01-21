"""Deck class"""
"""A Deck collaborates with Card and Shoe"""
"""It is responsible for creating all 52 cards from the Card class
   to be delivered to the Shoe"""


class Deck:
    """The deck will collect all 52 cards. It will be able to shuffle"""
    def __init__(self, Card):

        self.ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J",
                      "Q", "K", "A"]
        self.suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

        deck = [Card(name, suit) for rank in self.ranks for suit in self.suits]
        return deck
        print deck

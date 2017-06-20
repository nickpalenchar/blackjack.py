# -*- coding: utf-8 -*-
import random

class Card:
    def __init__(self, val, suit):
        self.val = str(val)
        self.suit = suit
        if(suit == "H" or suit == "D"):
            self.color = "RED"
        else:
            self.color = "BLACK"
    def __str__(self):
        suitSym = None
        if(self.suit == "H"):
            suitSym = "\u2661" # ♥︎
        if(self.suit == "S"):
            suitSym = "\u2660" # ♠
        if(self.suit == "D"):
            suitSym = "\u2662"
        if(self.suit == "C"):
            suitSym = "\u2663"
        return "%s%s" % (self.val, suitSym)

class Deck:
    def __init__(self, CardClass):
        vals = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        suits = ['H','S','D','C']
        self.stack = []
        for val in vals:
            for suit in suits:
                self.stack.append(CardClass(val, suit))
        random.shuffle(self.stack)
    def __len__(self):
        return len(self.stack)
    def deal(self):
        if(not len(self)):
            return None
        return self.stack.pop()


deck = Deck(Card)
print(deck.deal())

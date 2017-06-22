from card_class import Deck
from bj_class import BjCard

class PlayerHand:
    def __init__(self):
        self.hand = []
    def __str__(self):
        strHand = ""
        score = 0
        for card in self.hand:
            strHand += str(card) + " "
            score += card
        return ("%s | %d" % (strHand, score))
    def getCardFromDeck(self, deck):
        self.hand.append(deck.deal())
        return self
    def _getScore(self):
        score = 0
        for card in self.hand:
            score += card
        return score
    def isBust(self):
        return self._getScore() > 21

deck = Deck(BjCard)
hand = PlayerHand()

#print(hand)
hand.getCardFromDeck(deck).getCardFromDeck(deck).getCardFromDeck(deck)

print(hand)
print(hand.isBust())


class Game:
    def __init__(self):
        self.money = 100
        self.state = None

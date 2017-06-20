from card_class import Deck
from card_class import Card

card_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

class BjCard(Card):
    def __add__(self, other):
        ace = False
        if self.val == 'A' or other.val == 'A':
            ace = True
        subtotal = card_values[self.val] + card_values[other.val]
        if subtotal > 21 and ace:
            subtotal -= 10 # Ace changes value from 11 to 1
        return subtotal
    def __radd__(self, other):
        return self.__add__(BjCard(other, 'H'))

deck = Deck(BjCard)
card1 = deck.deal()
card2 = deck.deal()
card3 = deck.deal()

print("%s, %s, %s\n %d" % (card1, card2, card3, card1 + card2 + card3))

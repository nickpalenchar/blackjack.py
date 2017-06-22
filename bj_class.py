from card_class import Deck
from card_class import Card

card_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

class BjCard(Card):
    def __add__(self, other):
        ace = False
        if self.val == 'A' or other.val == 'A':
            ace = True
        try:
            subtotal = card_values[self.val] + card_values[other.val]
        except KeyError:
            subtotal = card_values[self.val] + int(other.val)
        if subtotal > 21 and ace:
            subtotal -= 10 # Ace changes value from 11 to 1
        return subtotal
    def __radd__(self, other):
        if other == 11:
            return self.__add__(BjCard('A','H'))
        else:
            return self.__add__(BjCard(other, 'H'))
    def __str__(self):
        return super(BjCard, self).__str__()

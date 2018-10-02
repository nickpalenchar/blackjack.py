from random import randint

class Card:
    def __init__(self, value:str, suit:str):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return self.__str__()

    def __str__(self):

        suit_dict = { 'H': '♥',
                      'S': '♠',
                      'D': '♦︎',
                      'C': '♣︎',}
        value_list = [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return value_list[self.value] + suit_dict[self.suit]


class Deck:
    def __init__(self):
        
        self.stack = []

        for i in range (1,14):
            self.stack += [Card(i, suit) for suit in {'H', 'S', 'D', 'C'}] 

    def __len__(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if not len(self.stack):
            return None
        return self.stack.pop()

    def shuffle(self):
        end = len(self.stack) - 1
        for edge in range(len(self.stack) - 1):
            selectedindex = randint(edge, end)
            self.stack[edge], self.stack[selectedindex] = self.stack[selectedindex], self.stack[edge]

if __name__ == '__main__':
    d = Deck()
    d.shuffle()
    print(d.stack)
    d.shuffle()
    print(d.stack)

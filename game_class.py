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
        return (isinstance(DealerHand), "YOU:\n%s | %d" % (strHand, score))
    def getCardFromDeck(self, deck):
        self.hand.append(deck.deal())
        return self
    def getScore(self):
        score = 0
        for card in self.hand:
            score += card
        return score
    def isBust(self):
        return self.getScore() > 21

class DealerHand(PlayerHand):
    def __init__(self):
        super().__init__()
        self.revealed = False
    def __str__(self):
        strHand = "** "
        score = 0
        for index, card in enumerate(self.hand):
            if index == 0:
                continue
            strHand += str(card) + " "
            score += card
        return ("DEALER:\n%s | %d?" % (strHand, score))
    def reveal(self):
        self.revealed = True
    def hide(self):
        self.revealed = False


dealer = DealerHand()
print("dealer hand" , dealer)


deck = Deck(BjCard)
dealer.getCardFromDeck(deck).getCardFromDeck(deck)
print(dealer)
hand = PlayerHand()

#print(hand)
hand.getCardFromDeck(deck).getCardFromDeck(deck).getCardFromDeck(deck)



class Game:
    def __init__(self):
        self.money = 100
        self.state = None
        self.bet = 0
        self.startBet()
    def startBet(self):
        print("Money: %d" % self.money)
        bet = None
        while not isinstance(bet, int) or int == 0 or int > self.money:
            try:
                bet = int(input("enter your bet: "))
            except ValueError:
                print("You must enter a number")
                #TODO go to top of while loop
            if int < 1:
                print("You must bet at least 1")
            elif int > self.money:
                print("You can't bet more than you have")
        self.bet = bet
        self.startDeal()
    def startDeal(self):
        pass


#game = Game()

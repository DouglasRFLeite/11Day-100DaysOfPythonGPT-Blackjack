from deck_of_cards import Deck


class Dealer:
    def __init__(self):
        self.hand = []

    def drawCard(self, deck, face="down"):
        if deck.getSize():
            self.hand.append([deck.getCard(), face])

    def lookAtHand(self):
        print("Dealers Hand:")
        hand = ""
        for card in self.hand:
            if card[1] == "up":
                hand += card[0] + " - "
            else:
                hand += "Hidden Card - "
        print(hand)

    def handSum(self):
        hand_sum = 0
        for card in self.hand:
            hand_sum += Deck.getCardValue(card[0])
        return hand_sum

    def hasBlackJack(self) -> bool:
        return self.handSum() == 21

    def hasBust(self) -> bool:
        return self.handSum() > 21

    def play(self, deck) -> None:
        while self.handSum() < 16 and deck.getSize():
            self.drawCard(deck)

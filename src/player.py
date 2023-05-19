from deck_of_cards import Deck


class Player:
    def __init__(self):
        self.hand = []

    def drawCard(self, deck, face="down"):
        if deck.getSize():
            self.hand.append([deck.getCard(), face])

    def lookAtHand(self):
        print("Players Hand:")
        hand = ""
        for card in self.hand:
            hand += card[0] + " - "

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
        while (not self.hasBlackJack()) and (not self.hasBust()):
            players_choice = input("Do you want to draw another card? [Y/N] ").lower()
            if players_choice == "y":
                self.drawCard(deck)
                self.lookAtHand()
            else:
                break
            
    def finalMessage(self, dealers_hand, players_hand):
        print(f"Dealers Hand: {dealers_hand} | Your Hand: {players_hand}")
        print("Congratulations! You win!")


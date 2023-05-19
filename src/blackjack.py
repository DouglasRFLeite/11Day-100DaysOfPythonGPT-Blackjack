from deck_of_cards import Deck
from dealer import Dealer
from player import Player

def choose_winner(dealer, player):
    if dealer.hasBlackJack():
        return dealer
    elif player.hasBlackJack():
        return player
    elif dealer.hasBust():
        return player
    elif player.hasBust():
        return dealer
    elif dealer.handSum() >= player.handSum():
        return dealer
    else:
        return player


def blackjack():
    print("Welcome to Blackjack.py! You will play against the dealer.")
    dealer = Dealer()
    player = Player()
    deck = Deck()

    dealer.drawCard(deck, face="up")
    player.drawCard(deck, face="up")
    dealer.drawCard(deck, face="down")
    player.drawCard(deck, face="down")
    
    dealer.lookAtHand()
    player.lookAtHand()
    
    dealer.play(deck)
    player.play(deck)

    winner = choose_winner(dealer, player)
    winner.finalMessage(dealer.handSum(), player.handSum())


if __name__ == "__main__":
    blackjack()

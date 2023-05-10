from deck_of_cards import Deck
from dealer import Dealer

def user_interface():
    print("Welcome to Blackjack.py! You will play against the dealer.")
    dealer = Dealer()
    player = Player()
    deck = Deck()

    dealer.draw_card(deck, face = "up")
    player.draw_card(deck, face = "up")
    dealer.draw_card(deck, face = "down")
    player.draw_card(deck, face = "down")

    dealer.play(player.lookAtHand())
    player.play()

    winner = choose_winner(dealer, player)
    print(final_message(winner))

if __name__ == "__main__":
    user_interface()


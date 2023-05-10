from deck_of_cards import Deck

class Dealer:
    def __init__(self):
        self.hand = []
    
    def draw_card(self, deck, face):
        self.hand.append([deck.getCard(), face])

    

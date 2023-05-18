from src.deck_of_cards import Deck
from os.path import abspath, dirname
import sys
import random
# Add the parent directory of the current file to sys.path
# sys.path.append(abspath(dirname(dirname(__file__))))

def test_Deck():
    deckOfCards = Deck()

    assert deckOfCards.getSize() == 52

    random.seed(1)
    card = deckOfCards.getCard()  # 9 of Hearts
    card_value = Deck.getCardValue(card)  # 9

    assert card_value == 9
    assert deckOfCards.getSize() == 51

    randnum = random.randint(0, 51)
    for _ in range(randnum):
        deckOfCards.getCard()

    assert deckOfCards.getSize() == (51-randnum)

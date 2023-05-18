from deck_of_cards import Deck
from dealer import Dealer
import random


def test_drawCard():
    dealer = Dealer()
    deck = Deck()
    random.seed(1)

    expected_hand = []
    assert dealer.hand == expected_hand

    dealer.drawCard(deck, face="up")
    expected_hand = [
        ["9 of Hearts", "up"]
    ]
    assert dealer.hand == expected_hand

    dealer.drawCard(deck, face="down")
    expected_hand = [
        ["9 of Hearts", "up"],
        ["Queen of Clubs", "down"]
    ]
    assert dealer.hand == expected_hand


def test_lookAtHand(capfd):
    dealer = Dealer()
    deck = Deck()

    # Call the function
    dealer.lookAtHand()

    # Capture the output
    captured = capfd.readouterr()
    output = captured.out.strip()

    # Assert the expected output
    expected_output = "Dealers Hand:"  # Replace with the expected output
    assert output == expected_output

    random.seed(1)

    dealer.drawCard(deck, face="up")
    dealer.drawCard(deck, face="down")

    # Call the function
    dealer.lookAtHand()

    # Capture the output
    captured = capfd.readouterr()
    output = captured.out.strip()

    # Replace with the expected output
    expected_output = "Dealers Hand:\n9 of Hearts - Hidden Card -"
    assert output == expected_output


def test_handSum():
    dealer = Dealer()
    deck = Deck()
    random.seed(1)

    dealer.drawCard(deck)
    dealer.drawCard(deck)

    assert dealer.handSum() == 19, dealer.lookAtHand()


def test_hasBlackJack():
    dealer = Dealer()
    dealer.hand = [
        ["9 of Hearts", "up"],
        ["10 of Hearts", "down"],
        ["2 of Hearts", "down"],
    ]

    assert dealer.handSum() == 21
    assert dealer.hasBlackJack()


def test_hasBust():
    dealer = Dealer()
    dealer.hand = [
        ["9 of Hearts", "up"],
        ["10 of Hearts", "down"],
        ["3 of Hearts", "down"],
    ]

    assert dealer.handSum() == 22
    assert dealer.hasBust()


def test_play():
    deck = Deck()
    dealer_stop = Dealer()
    dealer_stop.hand = [
        ["5 of Hearts", "up"],
        ["4 of Hearts", "down"],
    ]  # sum of 9

    random.seed(1)
    dealer_stop.play(deck)  # draws 9 of hearts and stops
    assert not dealer_stop.hasBlackJack()
    assert not dealer_stop.hasBust()
    assert dealer_stop.handSum() == 18

    deck.reset()
    dealer_blackjack = Dealer()
    dealer_blackjack.hand = [
        ["5 of Hearts", "up"],
        ["7 of Hearts", "down"],
    ]  # sum of 12

    random.seed(1)
    dealer_blackjack.play(deck)  # draws 9 of hearts and stops with BlackJack
    assert dealer_blackjack.hasBlackJack()
    assert not dealer_blackjack.hasBust()
    assert dealer_blackjack.handSum() == 21

    deck.reset()
    dealer_bust = Dealer()
    dealer_bust.hand = [
        ["Ace of Hearts", "up"],
        ["2 of Hearts", "down"],
    ]  # sum of 3

    random.seed(1)
    # draws 9 of hearts, draws queen of clubs and stops Busted
    dealer_bust.play(deck)
    assert not dealer_bust.hasBlackJack()
    assert dealer_bust.hasBust()
    assert dealer_bust.handSum() == 22

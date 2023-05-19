from deck_of_cards import Deck
from player import Player
import random


def test_drawCard():
    player = Player()
    deck = Deck()
    random.seed(1)

    expected_hand = []
    assert player.hand == expected_hand

    player.drawCard(deck, face="up")
    expected_hand = [
        ["9 of Hearts", "up"]
    ]
    assert player.hand == expected_hand

    player.drawCard(deck, face="down")
    expected_hand = [
        ["9 of Hearts", "up"],
        ["Queen of Clubs", "down"]
    ]
    assert player.hand == expected_hand


def test_lookAtHand(capfd):
    player = Player()
    deck = Deck()

    # Call the function
    player.lookAtHand()

    # Capture the output
    captured = capfd.readouterr()
    output = captured.out.strip()

    # Assert the expected output
    expected_output = "Players Hand:"  # Replace with the expected output
    assert output == expected_output

    random.seed(1)

    player.drawCard(deck, face="up")
    player.drawCard(deck, face="down")

    # Call the function
    player.lookAtHand()

    # Capture the output
    captured = capfd.readouterr()
    output = captured.out.strip()

    # Replace with the expected output
    expected_output = "Players Hand:\n9 of Hearts - Queen of Clubs -"
    assert output == expected_output


def test_handSum():
    player = Player()
    deck = Deck()
    random.seed(1)

    player.drawCard(deck)
    player.drawCard(deck)

    assert player.handSum() == 19, player.lookAtHand()


def test_hasBlackJack():
    player = Player()
    player.hand = [
        ["9 of Hearts", "up"],
        ["10 of Hearts", "down"],
        ["2 of Hearts", "down"],
    ]

    assert player.handSum() == 21
    assert player.hasBlackJack()


def test_hasBust():
    player = Player()
    player.hand = [
        ["9 of Hearts", "up"],
        ["10 of Hearts", "down"],
        ["3 of Hearts", "down"],
    ]

    assert player.handSum() == 22
    assert player.hasBust()

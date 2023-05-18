from src.deck_of_cards import Deck
from src.dealer import Dealer


def test_lookAtHand(capfd):
    dealer = Dealer()

    # Call the function
    dealer.lookAtHand()

    # Capture the output
    captured = capfd.readouterr()
    output = captured.out.strip()

    # Assert the expected output
    expected_output = "Dealers Hand:\n"  # Replace with the expected output
    assert output == expected_output

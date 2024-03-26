import pytest
from pycard import CardPool, Player  


def test_cardpool_initialization():
    cp = CardPool()
    assert len(cp.cards) == 52, f"Expected to get 52, but it returned{len(cp.cards)}"
    assert len(cp.players) == 0,f"Expected to get 0, but it returned{len(cp.players)}" 


def test_new_player():
    cp = CardPool()
    player = cp.newPlayer()
    assert len(cp.players) == 1, f"Expected to get 1, but get {len(cp.players)}"
    assert cp.players[0] == player, f"Wrong player input"
    assert player.name == "Player1", f"Expected to get Player1, but it returned {player.name}"


def test_draw():
    cp = CardPool()
    player = cp.newPlayer()
    card = player.draw()
    assert card == player.latest_card, "Wrong card"
    assert len(cp.cards) == 51, f"Expected to get 51, but get {len(cp.cards)}"


def test_compare(capfd):  # Use the capfd fixture to capture print outputs
    cp = CardPool()
    player1 = cp.newPlayer()
    player2 = cp.newPlayer()
    
    cp.cards = [{'suit': 'Hearts', 'value': 'Ace'}, {'suit': 'Spades', 'value': 'King'}]  
    
    player1.draw()  # Should draw the Ace of Hearts
    player2.draw()  # Should draw the King of Spades

    cp.compare()
    
    out, err = capfd.readouterr()
    assert "Player1 with the Ace of Hearts" in out, "Expected Player1 to win with the Ace of Hearts"


# Test running out of cards
def test_out_of_cards():
    cp = CardPool()
    cp.cards = []  # Empty the card pool
    with pytest.raises(Exception):  # Expecting an exception when trying to draw from an empty deck
        cp.draw()

# Test the game with no players
def test_compare_no_players(capfd):
    cp = CardPool()
    cp.compare()
    out, err = capfd.readouterr()
    assert "No players in the game." in out, "Expected message about no players in the game"
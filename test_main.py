from main import determine_winner
import pytest

@pytest.mark.parametrize("computer, player, expected", [
    ("rock", "scissors", "computer"),
    ("scissors", "rock", "player"),
    ("paper", "rock", "computer"),
    ("rock", "paper", "player"),
    ("scissors", "paper", "computer"),
    ("paper", "scissors", "player"),
    ("paper", "paper", "tie"),
    ("scissors", "scissors", "tie"),
    ("rock", "rock", "tie")
])
def test_determine_winner(computer, player, expected):
    assert determine_winner(computer, player) == expected
from main import determine_winner

def test_rock_beats_scissors():
    assert determine_winner("rock", "scissors") == "computer"
    assert determine_winner("scissors", "rock") == "player"

def test_paper_beats_rock():
    assert determine_winner("paper", "rock") == "computer"
    assert determine_winner("rock", "paper") == "player"

def test_scissors_beats_paper():
    assert determine_winner("scissors", "paper") == "computer"
    assert determine_winner("paper", "scissors") == "player"

def test_tie():
    assert determine_winner("paper", "paper") == "tie"
    assert determine_winner("scissors", "scissors") == "tie"
    assert determine_winner("rock", "rock") == "tie"
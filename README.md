# Rock Paper Scissors

A terminal-based Rock Paper Scissors game written in Python, with unit tests written in pytest.

## Requirements

- Python 3.10 or newer (the game uses the `match` statement)
- `pytest` (only needed to run the tests)

## How to run

```
python main.py
```

## How to play

1. Wait for the computer to make its choice (a short animation is shown).
2. Type `rock`, `paper` or `scissors` and press Enter.
3. The result is displayed together with both choices.

Rules:
- Rock beats scissors
- Scissors beats paper
- Paper beats rock

## Example

```
The computer chose.
Enter your choice: rock
You won! (rock > scissors)
```

## Running the tests

```
pip install -r requirements.txt
pytest -v
```

The tests cover all 9 choice combinations of `determine_winner` (computer win, player win, tie) using `pytest.mark.parametrize`.

## Features

- Play against the computer
- Input validation (case-insensitive, ignores extra spaces)
- Loading animation while the computer chooses
- Game logic separated from input/output (`determine_winner` returns the result)
- Unit tests for the game logic with pytest

## Planned features

- Tests for player input handling (using `monkeypatch`)
- Best-of-three mode with a score counter
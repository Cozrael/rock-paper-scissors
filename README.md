# Rock Paper Scissors

A terminal-based Rock Paper Scissors game written in Python.

## Requirements

- Python 3.10 or newer (the game uses the `match` statement)
- No external dependencies

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

## Features

- Play against the computer
- Input validation (case-insensitive, ignores extra spaces)
- Loading animation while the computer chooses
- Game logic separated from input/output (`determine_winner` returns the result)

## Planned features

- Unit tests with pytest
- Best-of-three mode with a score counter

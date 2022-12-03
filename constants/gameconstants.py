# Translate to score
ROCK = 1
PAPER = 2
SCISSORS = 3

# Player input dictionary
dictionary = {'A': ROCK, 'B': PAPER, 'C': SCISSORS, 'X': 'LOSS', 'Y': 'DRAW', 'Z': 'WIN'}
reverse_dictionary = {ROCK: 'A', PAPER: 'B', SCISSORS: 'C'}
loses_to = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}

find_weakness = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
}

# Game
WIN = 6
DRAW = 3
LOSS = 0

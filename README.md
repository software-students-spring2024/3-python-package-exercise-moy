# Python Package Exercise
[![log github events](https://github.com/software-students-spring2024/3-python-package-exercise-moy/actions/workflows/event-logger.yml/badge.svg)](https://github.com/software-students-spring2024/3-python-package-exercise-moy/actions/workflows/event-logger.yml)

## PyCard: A Simple Python Card Game Library

PyCard is a lightweight, easy-to-use Python package designed to simulate card games. It provides basic functionalities such as creating a deck of cards, shuffling, drawing cards, and comparing card values and suits between players.

## Functionalities

Deck creation with standard 52 playing cards.
Shuffle the deck and draw cards.
Support for multiple players.
Card comparison based on value and suit.

## Installation

how a developer who wants to import your project into their own code can do so - include documentation for all functions in your package and a link to an example Python program that uses each of them.
CardPool
A class representing a deck of 52 playing cards, including functionalities for shuffling, drawing cards, and comparing card values.
__init__()
Initializes a shuffled deck of cards.
newPlayer() -> Player
Adds a new player to the game and returns a Player object.
draw() -> dict
Draws a card from the deck. Raises an exception if the deck is empty.
Returns: A dictionary representing a card with suit and value.
compare()
Compares the latest drawn cards among all players and prints the winner.
Player
Represents a player in the game, capable of drawing cards from the deck.
__init__(pool: CardPool)
Associates the player with a specific CardPool.
draw() -> dict
Draws a card for the player from the associated CardPool.
Returns: A dictionary representing the drawn card.

## Contribution

We welcome contributions! That's how it can be done:

git clone https://github.com/your-github/pycard.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Team Members

Jinqiao Cheng       https://github.com/jinqiaocheng163
Yinyi Wen           https://github.com/YY35n
Zhengyang Han       https://github.com/Hmic1102

## Link to PyPl Page


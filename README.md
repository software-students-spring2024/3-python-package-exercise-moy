# Python Package Exercise

[![log github events](https://github.com/software-students-spring2024/3-python-package-exercise-moy/actions/workflows/event-logger.yml/badge.svg)](https://github.com/software-students-spring2024/3-python-package-exercise-moy/actions/workflows/event-logger.yml)

## PyCard: A Simple Python Card Game Library

#### PyCard is a lightweight, easy-to-use Python package designed to simulate card games. It provides basic functionalities such as creating a deck of cards, shuffling, drawing cards, and comparing card values and suits between players.


####   
```
3-python-package-exercise-moy/
 ├── src/
 │   └── pycard/
 │       ├── __init__.py
 │       └── pycard.py
 └── tests/
     ├── __init__.py
     └── testcards.py
 |____README.md
 |____LICENSE
 |____pyproject.toml
```
## Functionalities

#### Deck creation with standard 52 playing cards.
#### Shuffle the deck and draw cards.
#### Support for multiple players.
#### Card comparison based on value and suit.
  - Ace > King > Queen ... > 3 > 2 
  - ♠️ > ♦️ > ♥️ > ♣️
## Installation
#### Install
```bash
pip install -i https://test.pypi.org/simple/ pycard
```
#### Import
```python
from pycard.pycard import CardPool, Player
```

#### CardPool()
#### A class representing a deck of 52 playing cards, including functionalities for shuffling, drawing cards, and comparing card values.

```python
Board1 = CardPool()
```
#### CardPool.newPlayer() -> Player
#### Adds a new player to the game and returns a Player object.
```python
Jerry = Board1.newPlayer()
```
#### newPlayer.draw() -> dict
#### Draws a card from the deck. Raises an exception if the deck is empty.
```python
Jerry.draw()
```
#### Returns: A dictionary representing a card with suit and value.

#### CardPool.compare()
#### Compares the latest drawn cards among all players and prints the winner.
```python
Board1.compare()
```


## Contribution

#### We welcome contributions! That's how it can be done:
```bash
git clone https://github.com/software-students-spring2024/3-python-package-exercise-moy.git
```
```basg
python -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -i https://test.pypi.org/simple/ pycard
```
## Team Members of Group Moy

[**M**ichael (Zhengyang) Han](https://github.com/Hmic1102) 

[**O**liver (Jinqiao) Cheng](https://github.com/jinqiaocheng163)

[**Y**iwen Yin](https://github.com/YY35n)



## Link to PyPl Page

[Pycard](https://test.pypi.org/project/pycard/0.0.9/)

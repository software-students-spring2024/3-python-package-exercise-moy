import random

class CardPool:
    def __init__(self):
        self.suits_symbols = {'Spades': '♠', 'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣'}
        self.suits_hierarchy = ['Clubs', 'Diamonds', 'Hearts', 'Spades']  
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [{'suit': suit, 'value': value} for suit in self.suits_symbols for value in values]
        random.shuffle(self.cards)
        self.players = []

    def newPlayer(self):
        player = Player(self)
        self.players.append(player)
        return player

    def draw(self):
        if self.cards:
            return self.cards.pop()
        else:
            raise Exception("No cards left in the pool.")

    def compare(self):
        if not self.players:
            print("No players in the game.")
            return

        if not any(player.latest_card for player in self.players):
            print("No cards have been drawn.")
            return

        values_rank = {v: i for i, v in enumerate(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'], start=1)}
        winning_card = max(
            ((player, player.latest_card) for player in self.players if player.latest_card),
            key=lambda x: (values_rank[x[1]['value']], self.suits_hierarchy.index(x[1]['suit']))
        )
        winning_player, card = winning_card

        print(f"WOHOO: {winning_player.name} with the {card['value']} of {card['suit']} {self.suits_symbols[card['suit']]}.")

class Player:
    def __init__(self, pool):
        self.pool = pool
        self.latest_card = None
        self.name = f"Player{len(self.pool.players)+1}" 

    def draw(self):
        self.latest_card = self.pool.draw()
        suit_symbol = self.pool.suits_symbols[self.latest_card['suit']]
        print(f"{self.name} drew the {self.latest_card['value']} of {self.latest_card['suit']} {suit_symbol}.")
        return self.latest_card

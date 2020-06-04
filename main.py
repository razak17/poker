from game.card import Card
from game.deck import Deck
from game.hand import Hand
from game.player import Player

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand_1 = Hand(cards = [])
hand_2 = Hand(cards = [])

player_1 = Player(name="Razak", hand = hand_1)
player_2 = Player(name="Sue", hand=hand_1)

players = [player_1, player_2]


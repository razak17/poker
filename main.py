from game.card import Card
from game.deck import Deck
from game.hand import Hand
from game.player import Player

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)


from game.card import Card
from game.deck import Deck

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

# from main import deck, cards

print('Hello World')

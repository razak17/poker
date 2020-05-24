import unittest
from game.deck import Deck
from game.card import Card


class DeckTest(unittest.TestCase):
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(deck.cards, [])

    def test_add_cards_to_collection(self):
        card = Card(rank="Ace", suit="Spades")
        deck = Deck()
        deck.add_cards([card])

        self.assertEqual(deck.cards, [card])

import unittest
from unittest.mock import MagicMock

from game.card import Card
from game.hand import Hand
from game.player import Player


class PlayerTest(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand(cards=[])
        player = Player(name="Razak", hand=hand)
        self.assertEqual(player.name, "Razak")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Royal Flush"
        player = Player(name = "Boris", hand = mock_hand)
        self.assertEqual(
            player.best_hand(),
            "Royal Flush"
        )

        mock_hand.best_rank.assert_called()

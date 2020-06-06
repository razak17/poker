from game.card import Card
from game.deck import Deck
from game.game_round import GameRound
from game.hand import Hand
from game.player import Player

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player(name="Razak", hand=hand1)
player2 = Player(name="Sue", hand=hand2)

players = [player1, player2]

game_round = GameRound(deck=deck, players=players)
game_round.play()

# from main import deck, cards, game_round, hand1, hand2, player1, player2

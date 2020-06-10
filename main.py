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

for player in players:
    print(f"{player.name} receives a {player.hand}.")
    index, hand_name, hand_cards = player.best_hand()

    hand_cards_strings = [str(card) for card in hand_cards]
    hand_cards_sting = " and ".join(hand_cards_strings)
    print(f"{player.name} has a {hand_name} with a {hand_cards_sting}.")
winning_player = max(players)

print(f"{winning_player.name} wins.")

class Card():
    SUITS = ("Hearts", "Spades", "Diamonds", "Clubs")
    RANKS = (
        "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King", "Ace")

    @classmethod
    def create_standard_52_cards(cls):
        return [
            cls(rank=rank, suit=suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]

    def __init__(self, rank, suit):
        if type(rank) != str:
            raise ValueError(
                f"Rank must be a string. Try on of: {self.RANKS}")

        if rank not in self.RANKS:
            raise ValueError(
                f"Invalid rank. Rank must be on of: {self.RANKS}")

        if suit != suit.capitalize():
            raise ValueError(
                f"Suite must be capitalized. Try: {suit.capitalize()}")

        if suit not in self.SUITS:
            raise ValueError(
                f"Invalid suit. Suit must be on of: '{self.SUITS}'.")

        self.rank = rank
        self.suit = suit
        self.rank_index = self.RANKS.index(rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit

        return self.rank_index < other.rank_index

valid_suits = [
        "spades",
        "diamonds",
        "clubs",
        "hearts"
    ]
valid_ranks = [
    "ace",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "jack",
    "queen",
    "king"
]
rank_values = {rank: 14 if rank == "ace" else i for i, rank in enumerate(valid_ranks, start=1)}

class Suit:

    def __init__(self, suit: str):
        self._suit=self._verifySuit(suit)

    def __str__(self):
        return f"{self._suit}"

    def _verifySuit(self, suit: str) -> str:
        assert isinstance(suit, str), "Suit is not in a string format"
        assert suit.lower() in valid_suits, "Suit is not a valid option"
        return suit.lower()

    def _getSuit(self):
        return self._suit

class Rank:

    def __init__(self, rank: str):
        self._rank=self._verifyRank(rank)

    def __str__(self):
        return f"{self._rank}"

    def _verifyRank(self, rank: str):
        assert isinstance(rank, str), "Rank is not in string format"
        assert rank.lower() in valid_ranks, "Rank is not a valid option"
        return rank.lower()

    def _getRank(self):
        return self._rank

    def _getValue(self):
        return rank_values[self._rank]

class Card:

    def __init__(self, suit: str, rank: str):
        self._suit=Suit(suit)
        self._rank=Rank(rank)

    def __str__(self):
        return f"({self._suit},{self._rank})"

if __name__ == "__main__":
    print("Card class runs fine")

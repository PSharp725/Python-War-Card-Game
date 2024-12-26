import card
from random import shuffle

class Deck:

    def __init__(self):
        self._deck = self._buildDeck()

    def __str__(self):
        return "\n".join(str(card) for card in self._deck)

    def _buildDeck(self):
        deck = []
        for suit in card.valid_suits:
            for rank in card.valid_ranks:
                deck.append(card.Card(suit,rank))
        self._shuffleDeck(deck)
        return deck

    def _shuffleDeck(self, deck: list[card.Card]):
        return shuffle(deck)

if __name__ == "__main__":
    deck = Deck()
    print(deck)

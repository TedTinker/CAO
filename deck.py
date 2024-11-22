from copy import copy
from random import shuffle

from utils import RANKS, SUITS

class Card:
    """Represents a playing card with CAO attributes."""
    def __init__(self, rank, suit, character="(character)", action="(action)", obj="(object)"):
        self.rank = rank
        self.suit = suit
        self.character = character
        self.action = action
        self.obj = obj

    def __str__(self):
        """String representation of the card in CAO format."""
        return f"{self.rank}{self.suit}: {self.character} / {self.action} / {self.obj}"

    def __repr__(self):
        return self.__str__()

class Deck:
    """Manages a deck of cards."""
    def __init__(self):
        self.cards = [Card(r, s) for r in RANKS for s in SUITS]

    def shuffle(self):
        """Shuffles the deck."""
        shuffle(self.cards)

    def display_cao(self):
        """
        Groups cards in threes and displays their CAO attributes.
        Useful for memory palace creation or practice.
        """
        shuffled = copy(self.cards)
        self.shuffle()  # Ensure deck is shuffled
        while shuffled:
            # Extract cards in groups of three
            card_1 = shuffled.pop(0)
            card_2 = shuffled.pop(0) if shuffled else card_1
            card_3 = shuffled.pop(0) if shuffled else card_2

            # Print CAO format for the group
            print(f"({card_1.rank}{card_1.suit}, {card_2.rank}{card_2.suit}, {card_3.rank}{card_3.suit}): "
                  f"{card_1.character} / {card_2.action} / {card_3.obj}")

    def __str__(self):
        """String representation of the full deck."""
        return "\n".join(str(card) for card in self.cards)

# Main execution for testing
if __name__ == '__main__':
    deck = Deck()
    print("Shuffled Deck in CAO Format:")
    deck.display_cao()
from utils import RANKS, SUITS
from deck import Card, Deck

# Default CAO mappings for cards (empty for you to fill in)
DEFAULT_CAO = {
    # ♥ Hearts
    "♥": [
        ("",                     "",                 ""),  # A♥
        ("",                     "",                 ""),  # 2♥
        ("",                     "",                 ""),  # 3♥
        ("",                     "",                 ""),  # 4♥
        ("",                     "",                 ""),  # 5♥
        ("",                     "",                 ""),  # 6♥
        ("",                     "",                 ""),  # 7♥
        ("",                     "",                 ""),  # 8♥
        ("",                     "",                 ""),  # 9♥
        ("",                     "",                 ""),  # 10♥
        ("",                     "",                 ""),  # J♥
        ("",                     "",                 ""),  # Q♥
        ("",                     "",                 ""),  # K♥
    ],
    # ♦ Diamonds
    "♦": [
        ("",                     "",                 ""),  # A♦
        ("",                     "",                 ""),  # 2♦
        ("",                     "",                 ""),  # 3♦
        ("",                     "",                 ""),  # 4♦
        ("",                     "",                 ""),  # 5♦
        ("",                     "",                 ""),  # 6♦
        ("",                     "",                 ""),  # 7♦
        ("",                     "",                 ""),  # 8♦
        ("",                     "",                 ""),  # 9♦
        ("",                     "",                 ""),  # 10♦
        ("",                     "",                 ""),  # J♦
        ("",                     "",                 ""),  # Q♦
        ("",                     "",                 ""),  # K♦
    ],
    # ♤ Spades
    "♤": [
        ("",                     "",                 ""),  # A♤
        ("",                     "",                 ""),  # 2♤
        ("",                     "",                 ""),  # 3♤
        ("",                     "",                 ""),  # 4♤
        ("",                     "",                 ""),  # 5♤
        ("",                     "",                 ""),  # 6♤
        ("",                     "",                 ""),  # 7♤
        ("",                     "",                 ""),  # 8♤
        ("",                     "",                 ""),  # 9♤
        ("",                     "",                 ""),  # 10♤
        ("",                     "",                 ""),  # J♤
        ("",                     "",                 ""),  # Q♤
        ("",                     "",                 ""),  # K♤
    ],
    # ♧ Clubs
    "♧": [
        ("",                     "",                 ""),  # A♧
        ("",                     "",                 ""),  # 2♧
        ("",                     "",                 ""),  # 3♧
        ("",                     "",                 ""),  # 4♧
        ("",                     "",                 ""),  # 5♧
        ("",                     "",                 ""),  # 6♧
        ("",                     "",                 ""),  # 7♧
        ("",                     "",                 ""),  # 8♧
        ("",                     "",                 ""),  # 9♧
        ("",                     "",                 ""),  # 10♧
        ("",                     "",                 ""),  # J♧
        ("",                     "",                 ""),  # Q♧
        ("",                     "",                 ""),  # K♧
    ],
}

class EnhancedDeck(Deck):
    """Extended Deck to include CAO attributes."""
    def __init__(self, cao_mappings):
        self.cards = []
        for suit in SUITS:
            for rank, (character, action, obj) in zip(RANKS, cao_mappings[suit]):
                self.cards.append(Card(rank, suit, character, action, obj))

# Main script
if __name__ == "__main__":
    # Create a deck with default CAO mappings
    deck = EnhancedDeck(DEFAULT_CAO)

    # Shuffle and display the deck
    deck.shuffle()
    print("Shuffled Deck in CAO Format:")
    deck.display_cao()
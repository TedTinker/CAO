import argparse

# Argument parser setup
parser = argparse.ArgumentParser(description="Generate and shuffle a deck of cards in CAO format.")
try:
    args = parser.parse_args()
except:
    args, _ = parser.parse_known_args()


# Constants for ranks and suits
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUITS = ["♥", "♦", "♤", "♧"]  # Suits in a standard deck
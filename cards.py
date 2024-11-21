#%%

from copy import copy
from random import shuffle

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♥", "♦", "♤", "♧"] # ♠ ♥ ♦ ♣ ♤ ♡ ♢ ♧

class Card:
    
    def __init__(self, r, s, c = "(character)", a = "(action)", o = "(object)"):
        self.r = r ; self.s = s 
        self.c = c ; self.a = a ; self.o = o
        
    def __str__(self):
        return("{}{}\t: {} / {} / {}.".format(self.r, self.s, self.c, self.a, self.o))
    
    def __repr__(self):
        return(self.__str__ + "REPR")
    
    
    
class Deck: 
    
    def __init__(self, cards):
        self.cards = cards 
        
    def make_palace(self):
        shuffled = copy(self.cards)
        shuffle(shuffled)
        while shuffled != []:
            card_1 = shuffled.pop(0)
            card_str = card_1.r + card_1.s
            post_card_str = "\t"
            if(shuffled == []): card_2 = card_1 ; post_card_str += "\t"
            else:               
                card_2 = shuffled.pop(0)
                card_str += ", " + card_2.r + card_2.s
            if(shuffled == []): card_3 = card_2 ; post_card_str += "\t"
            else:               
                card_3 = shuffled.pop(0)
                card_str += ", " + card_3.r + card_3.s
                
            
                
            print("({}){}{} / {} / {}.".format(
                card_str, post_card_str, card_1.c, card_2.a, card_3.o))
        
    def __str__(self):
        to_return = ""
        for i, card in enumerate(self.cards):
            to_return += card.__str__() 
            if(i+1 != len(self.cards)): to_return += "\n"
        return(to_return)
    


card_list = [
    Card("A", "♥", "Faith",             "in a staring-contest with",        "Anihilato"),
    Card("2", "♥", "Slushi",            "teaches Sody Pop about",           "Ramune"),
    Card("3", "♥", "Chikn",             "becoming long, wrapping",          "cheez"),
    Card("4", "♥", "Cofi",              "scaring Iscream with",             "a herd of sheep"),
    Card("5", "♥", "Fwench Fwy",        "throwing bees at",                 "Hawt Saus"),
    Card("6", "♥", "Pikacho",           "thunderbolting",                   "Ash Ketchum"),
    Card("7", "♥", "Team Rocket",       "blasting off again because of",    "MewTwo"),
    Card("8", "♥", "Legendary Birds",   "shooting ice, static, and fire at","Lugia"),
    Card("9", "♥", "Twilight Sparkle",  "makes Spike barf lesson",          "a scroll"),
    Card("10","♥", "Flutterfy",         "choking on",                       "Iron Will"),
    Card("J", "♥", "Pinkie Pie",        "inflating",                        "a balloon"),
    Card("Q", "♥", "Rainbow Dash",      "flying to create",                 "a rainbow"),
    Card("K", "♥", "Celestia",          "imprisoning, on the moon,",        "Luna")
    ]
    
"""
    
    Card("A", "♦"), 
    Card("2", "♦"),
    Card("3", "♦"),
    Card("4", "♦"),
    Card("5", "♦"),
    Card("6", "♦"),
    Card("7", "♦"),
    Card("8", "♦"),
    Card("9", "♦"),
    Card("10","♦"),
    Card("J", "♦"),
    Card("Q", "♦"),
    Card("K", "♦"),
    
    Card("A", "♤"),
    Card("2", "♤"),
    Card("3", "♤"),
    Card("4", "♤"),
    Card("5", "♤"),
    Card("6", "♤"),
    Card("7", "♤"),
    Card("8", "♤"),
    Card("9", "♤"),
    Card("10","♤"),
    Card("J", "♤"),
    Card("Q", "♤"),
    Card("K", "♤"),
    
    Card("A", "♧"), # TF2 and other games
    Card("2", "♧"),
    Card("3", "♧"),
    Card("4", "♧"),
    Card("5", "♧"),
    Card("6", "♧"),
    Card("7", "♧"),
    Card("8", "♧"),
    Card("9", "♧"),
    Card("10","♧"),
    Card("J", "♧"),
    Card("Q", "♧"),
    Card("K", "♧"),
    ]
"""
deck = Deck(card_list)

print()
print(deck)
print()



deck.make_palace()
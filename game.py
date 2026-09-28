import random
import os


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} av {self.suit}"

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def make_deck():
        suits = ["Hjärter", "Ruter", "Klöver", "Spader"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        
        deck_cards = [Card(val, suit) for suit in suits for val in values]
        random.shuffle(deck_cards)
        return deck_cards

    def deal(self, num):
        dealt = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def take_cards(self, cards):
        self.hand.extend(cards)

    def play_card(self):
        return self.hand.pop(0)


def play_game():
    card_ranks = {
        2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
        8: 8, 9: 9, 10: 10, "J": 11, "Q": 12, "K": 13, "A": 14
    }

    cards = Deck.make_deck()
    deck = Deck(cards)

    player1 = Player("Spelare 1")
    player2 = Player("Spelare 2")

    player1.take_cards(deck.deal(1))
    player2.take_cards(deck.deal(1))

    c1 = player1.play_card()
    c2 = player2.play_card()

    v1 = card_ranks[c1.value]
    v2 = card_ranks[c2.value]

    type1 = "lågt kort" if v1 <= 7 else "högt kort"
    type2 = "lågt kort" if v2 <= 7 else "högt kort"

    #os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{player1.name} drog: {c1} ({type1})")
    print(f"{player2.name} drog: {c2} ({type2})")

    if v1 > v2:
        print(f"{player1.name} vinner med högst kort!")
    elif v2 > v1:
        print(f"{player2.name} vinner med högst kort!")
    else:
        print("Det blev oavgjort!")



while True:
    play_game()

    answer = input("Vill du spela igen? (ja/nej): ").strip().lower()

    if answer != "ja":
        break
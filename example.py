class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __iter__(self):
        return (self.rank, self,suit)
    def __str__(self):
        a=str(self.rank) +' '+ str(self.suit)
        return a
class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    def __iter__(self):
        return iter(self.cards)
deck = Deck()
for card in deck:
    print(card)
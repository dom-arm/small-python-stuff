from random import shuffle


class Deck:
    # The deck consists of 52 cards in total
    suite = "H D S C".split()
    ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self):
        self.cards = []

        # Populate cards list (52 / 4 = 13)
        for i in range(13):
            self.cards.append((Deck.suite[0], Deck.ranks[i]))
            self.cards.append((Deck.suite[1], Deck.ranks[i]))
            self.cards.append((Deck.suite[2], Deck.ranks[i]))
            self.cards.append((Deck.suite[3], Deck.ranks[i]))

    def shuffle(self):
        shuffle(self.cards)
        return self.cards

    def split(self):
        return self.cards[:26], self.cards[26:]

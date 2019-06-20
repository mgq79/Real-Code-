import random
from Card import Card

class SetDeck(object):
    def __init__(this):
        this.deck = []
        for color in range(3):
            for shape in range(3):
                for count in range(3):
                    for fill in range(3):
                        this.deck.append(Card(color, shape, count, fill))

    def size(this):
        return len(this.deck)

    def draw(this):
        c = this.deck.pop(random.randrange(this.size()))
        return c


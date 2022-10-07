

from random import shuffle


class deck:

    def __init__(self):
        suite = 'H D S C'.split()
        ranks = '2 3 4 5 6 7 8 9 10 j q k a'.split()
        print('creating new deck')
        self.allcards = [(s, r) for s in suite for r in ranks]

    def shuffle(self):
        print('shuffling deck')
        shuffle(self.allcards)

    def half(self):
        return (self.allcards[:26], self.allcards[26:])

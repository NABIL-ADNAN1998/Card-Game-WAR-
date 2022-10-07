



class hand:

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "contains {} ".format(len(self.cards))

    def add(self, add_cards):
        self.cards.extend(add_cards)

    def remove_cards(self):
        return self.cards.pop()

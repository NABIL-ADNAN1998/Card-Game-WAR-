



class player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_cards()
        print("{} has placed {} ".format(self.name, drawn_card))
        print('\n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if (len(self.hand.cards) < 3):
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        return (len(self.hand.cards)) != 0

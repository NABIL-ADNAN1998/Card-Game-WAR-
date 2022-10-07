from random import shuffle
from deck_class import deck
from hand_class import hand
from player_class import player


suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 j q k a'.split()

d = deck()
d.shuffle()
half1, half2 = d.half()
comp = player('computer', hand(half1))

name = input('set your name: -> ')
user = player(name, hand(half2))

total_rounds = 0
war_counts = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print('time for a new round')
    print('here is the standings')
    print(user.name + ' has the count: ' + str(len(user.hand.cards)))
    print(comp.name + ' has the count: ' + str(len(comp.hand.cards)))
    print('play a card')
    print('\n')

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()
    table_cards.append(c_card)
    table_cards.append(p_card)

    if (c_card[1] == p_card[1]):
        war_counts += 1
        print("war")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        if (ranks.index(c_card[1]) < ranks.index(p_card[1])):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if (ranks.index(c_card[1]) < ranks.index(p_card[1])):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print('game over.number of rounds: ' + str(total_rounds))
print('a war happend ' + str(war_counts) + " times")

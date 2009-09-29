#!/usr/bin/python

import cards
from cards import shuffle, cardSorted

def deal(deck, numShuffle=7):
    for y in range(numShuffle):
        deck = shuffle(deck) 
    hands = list()
    for player in range(4):
        hands.append(cardSorted([deck[x] for x in range(player, len(deck), 4)]))
    return hands

def prettyHand(hand):
    pretty = list()
    suit = ''
    for card in reversed(hand):
        if suit != card[0]:
            if suit != '':
                pretty.append('\n')
            suit = card[0]
            pretty.append(suit)
        pretty.append(card[1])
    return ''.join(pretty)

if __name__ == '__main__':
    hands = deal(cards.deck)
    player = 1
    for hand in hands:
        print "Player", player
        print prettyHand(hand)
        print
        player += 1

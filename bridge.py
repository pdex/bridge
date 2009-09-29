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

def prettyHand(hand, defensiveTricks=dict(), hcp=dict()):
    pretty = list()
    suit = ''
    for card in reversed(hand):
        if suit != card[0]:
            if suit != '':
                if defensiveTricks.has_key(suit):
                    pretty.append(" Q/D tricks: %s" % ", ".join(defensiveTricks[suit]))
                if hcp.has_key(suit):
                    pretty.append(" HCP: %s" % ", ".join(hcp[suit]))
                pretty.append('\n')
            suit = card[0]
            pretty.append(suit)
        pretty.append(card[1])
    #gah this edge condition sucks, need to find a better way.
    if defensiveTricks.has_key(suit):
        pretty.append(" Q/D tricks: %s" % ", ".join(defensiveTricks[suit]))
    if hcp.has_key(suit):
        pretty.append(" HCP: %s" % ", ".join(hcp[suit]))
    return ''.join(pretty)

trickTable = (
    ('AK', 2  ),
    ('AQ', 1.5),
    ('KQ', 1  ),
    ('A' , 1  ),
    ('K0', 0.5),
    ('K9', 0.5),
    ('K8', 0.5),
    ('K7', 0.5),
    ('K6', 0.5),
    ('K5', 0.5),
    ('K4', 0.5),
    ('K3', 0.5),
    ('K2', 0.5),
)

def suitContains(suit, cards):
    for card in cards:
        if suit.find(card) == -1:
            return False
    return True

def filterSuit(suit, cards):
    for card in cards:
        suit = suit.replace(card, '')
    return suit

def defensiveTricks(hand, annotate=dict()):
    tricks = 0
    for suit in cards.suits:
        suitCards = ''.join(map(lambda x: x[1], filter(lambda x: x[0] == suit, hand)))
        for row in trickTable:
            if suitContains(suitCards, row[0]):
                tricks += row[1]
                suitCards = filterSuit(suitCards, row[0])
                annotate.setdefault(suit, list()).append("%s : %1.1f" % row)
            if len(suitCards) == 0:
                break
    return tricks

hcpTable = (
    ('A', 4),
    ('K', 3),
    ('Q', 2),
    ('J', 1),
)

def hcpCount(hand, annotate=dict()):
    points = 0
    for suit in cards.suits:
        suitCards = ''.join(map(lambda x: x[1], filter(lambda x: x[0] == suit, hand)))
        for row in hcpTable:
            if suitCards.find(row[0]) != -1:
                points += row[1]
                annotate.setdefault(suit, list()).append("%s : %d" % row)
        length = len(suitCards)
        if length > 4:
            addPoints = length - 4
            points += addPoints
            annotate.setdefault(suit, list()).append("length(%d): +%d" % (length, addPoints))
    return points

if __name__ == '__main__':
    hands = deal(cards.deck)
    player = 1
    for hand in hands:
        dt = {}
        hcp = {}
        print "Player", player, "Quick/Defensive tricks:", defensiveTricks(hand, dt), "HCP:", hcpCount(hand, hcp)
        print prettyHand(hand, defensiveTricks=dt, hcp=hcp)
        print
        player += 1

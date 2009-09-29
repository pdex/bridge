#!/usr/bin/python

import random

cards = tuple(map(str, [y for y in range(2, 10)]) + ['0', 'J', 'Q', 'K', 'A'])

cmpTable = ''.join(cards)

suits = ('C', 'D', 'H', 'S')

deck = tuple(x + y for x in suits for y in cards)

def shuffle(old):
    new = list(old)
    random.shuffle(new)
    return new

def cmpFunc(a, b):
    result = cmp(a[0],b[0])
    if result == 0:
        result = cmp(cmpTable.find(a[1]),cmpTable.find(b[1]))
    return result

def cardSorted(cards):
    return sorted(cards, cmpFunc)

if __name__ == '__main__':
    print deck
    print shuffle(deck)
    print cardSorted(shuffle(deck))

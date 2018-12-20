#!/usr/bin/python

import sys
import itertools
from recordclass import recordclass

def main():
    squares = [[]]
    two_letters = 0
    three_letters = 0
    ids = []
    overlaps = set()
    seen = {}

    for claim in open(sys.argv[1]):
        Square = recordclass('Square', 'x1 y1 x2 y2')
        tmp = claim.split('@')[-1].strip().split(': ')
        square1 = Square(*(map(int, tmp[0].split(',')) + map(int, tmp[1].split('x'))))
        square1.x2 += square1.x1
        square1.y2 += square1.y1
        x1 = range(square1.x1, square1.x2)
        y1 = range(square1.y1, square1.y2)
        ids.append((x1, y1))

    for pair in itertools.combinations(ids, r=2):
        xs = set(pair[0][0])
        ys = set(pair[0][1])
        overlapx = xs.intersection(pair[1][0])
        overlapy = ys.intersection(pair[1][1])
        for x in overlapx:
            for y in overlapy:
                overlaps.add((x,y))

    print(len(overlaps))

main()



"""
Scrabble Hand
Given an array of scrabble tiles,
    create a function that outputs the maximum possible score a player can achieve
    by summing up the total number of points for all the tiles in their hand.
    Each hand contains 7 scrabble tiles.
"""
from unittest import TestCase

tile, score = 'tile', 'score'
arg, expected = 'arg', 'expected'


def max_score(tile_set):
    return sum(x['score'] for x in tile_set)
    # return sum(tile_set.values())


class TestMaxScore(TestCase):

    data = [
        {
            arg: [
                {tile: "N", score: 1},
                {tile: "K", score: 5},
                {tile: "Z", score: 10},
                {tile: "X", score: 8},
                {tile: "D", score: 2},
                {tile: "A", score: 1},
                {tile: "E", score: 1}
            ],
            expected: 28
        },
        {
            arg: [
                {tile: "B", score: 2},
                {tile: "V", score: 4},
                {tile: "F", score: 4},
                {tile: "U", score: 1},
                {tile: "D", score: 2},
                {tile: "O", score: 1},
                {tile: "U", score: 1}
            ],
            expected: 15
        }
    ]

    def test_data(self):
        for entry in self.data:
            assert max_score(entry[arg]) == entry[expected]

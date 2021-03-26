from unittest import TestCase
from tools.games.go_fish_checker import numpy_check_golf as check


class TestGoFish(TestCase):

    def test_same_color(self):
        assert check([
            {'color': "red", 'number': 1, 'shade': "empty", 'shape': "squiggle"},
            {'color': "red", 'number': 2, 'shade': "lined", 'shape': "diamond"},
            {'color': "red", 'number': 3, 'shade': "full", 'shape': "oval"}
        ]) is True

    def test_colors_partial_different(self):
        assert check([
            {'color': "red", 'number': 1, 'shade': "empty", 'shape': "squiggle"},
            {'color': "red", 'number': 2, 'shade': "lined", 'shape': "diamond"},
            {'color': "purple", 'number': 3, 'shade': "full", 'shape': "oval"}
        ]) is False

    def test_match_color_different_number(self):
        assert check([
            {'color': "green", 'number': 1, 'shade': "empty", 'shape': "squiggle"},
            {'color': "green", 'number': 2, 'shade': "empty", 'shape': "diamond"},
            {'color': "green", 'number': 3, 'shade': "empty", 'shape': "oval"}
        ]) is True

    def test_diff_color_same_else(self):
        assert check([
            {'color': "purple", 'number': 1, 'shade': "full", 'shape': "oval"},
            {'color': "green", 'number': 1, 'shade': "full", 'shape': "oval"},
            {'color': "red", 'number': 1, 'shade': "full", 'shape': "oval"}
        ]) is True

    def test_diff_color_mix_number_match_else(self):
        assert check([
            {'color': "purple", 'number': 3, 'shade': "full", 'shape': "oval"},
            {'color': "green", 'number': 1, 'shade': "full", 'shape': "oval"},
            {'color': "red", 'number': 3, 'shade': "full", 'shape': "oval"}
        ]) is False

"""In the game Set, three cards form a set if each of the cards are identical or completely different for each of the four properties. All three cards must:

    Have the same color or different colors.
    Have the same number or different numbers.
    Have the same shades or different shades.
    Have the same shape or different shapes.

The four properties are:

    Colors: red, purple, green
    Numbers: 1, 2, 3
    Shades: empty, lined, full
    Shapes: squiggle, oval, diamond
"""


def check_set(card_set):
    """
    Decide whether the three cards meet the criteria for a set
    :param card_set: should contain three cards
    :return: True/False
    """
    allowed = 1, 3
    colors = set([])
    numbers = set([])
    shades = set([])
    shapes = set([])
    for card in card_set:
        colors.add(card['color'])
        numbers.add(card['number'])
        shades.add(card['shade'])
        shapes.add(card['shape'])
    check_colors = len(colors) in allowed
    check_numbers = len(numbers) in allowed
    check_shades = len(shades) in allowed
    check_shapes = len(shapes) in allowed
    if check_colors and check_numbers and check_shades and check_shapes:
        return True
    else:
        return False


def numpy_check_set(card_set):
    import numpy as np
    # Create Numpy Array where each card is a row
    # property names are not needed
    cards = np.array([list(card.values()) for card in card_set])
    # Transpose of Array allows iteration on columns
    # sets remove duplicates before len counts those unique values
    counts = [len(set(this_prop)) for this_prop in cards.T]
    return 2 not in counts


def numpy_check_golf(card_set):
    import numpy
    return 2 not in [len(set(this_prop))for this_prop in numpy.array([list(card.values()) for card in card_set]).T]

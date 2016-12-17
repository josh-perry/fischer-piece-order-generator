'''
White pawns are placed on the second rank as in standard chess.
All remaining white pieces are placed randomly on the first rank, with two restrictions:

* The bishops must be placed on opposite-color squares.
* The king must be placed on a square between the rooks.
Black's pieces are placed equal-and-opposite to White's pieces.
'''

import random

# Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook
pieces = ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R']


def check_king_rook_rule(layout):
    rooks_found = 0

    for piece in layout:
        if piece == 'K' and rooks_found == 1:
            return True

        if piece == 'R':
            rooks_found += 1

    return False


def check_bishop_rule(layout):
    rook_indices = [i for i, x in enumerate(layout) if x == 'B']

    even_indices = [i for i, x in enumerate(rook_indices) if x % 2 == 0]
    odd_indices = [i for i, x in enumerate(rook_indices) if x % 2 != 0]

    if len(even_indices) == 1 and len(odd_indices) == 1:
        return True

    return False


def is_layout_good(layout):
    good = check_king_rook_rule(layout) and check_bishop_rule(layout)
    return good


def main():
    random.shuffle(pieces)

    while not is_layout_good(pieces):
        random.shuffle(pieces)

    print("".join(pieces))

if __name__ == '__main__':
    main()

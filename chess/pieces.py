""" Pieces Module (entities) """
from chess.constants import *


class Piece:
    """ Parent class for all chess pieces """

    unit_dict = {
        'Pawn': 'p',
        'Rook': 'r',
        'Night': 'n',
        'Bishop': 'b',
        'Queen': 'q',
        'King': 'k',
        'Piece': 'x'
    }

    def __init__(self, row, col, is_white):
        self.row = row
        self.col = col
        self.is_white = is_white  # bool

        self.unit = self.unit_dict[self.__class__.__name__]

        if self.is_white:
            self.name = 'w' + self.unit
        else:
            self.name = 'b' + self.unit

    def __repr__(self):
        return self.__class__.__name__ + \
            f"({self.row}, {self.col}, is_white={self.is_white})"

    def get_moves(self, game):
        raise NotImplementedError


class Pawn(Piece):
    """Ruleset for pawns"""

    def __init__(self, row, col, is_white, first_move=True):
        super().__init__(row, col, is_white)
        self.first_move = first_move

    def get_moves(self, game):
        moves = []
        fwd = -1 if self.is_white is True else 1

        # basic move
        if isinstance(game[(self.row + fwd, self.col)], Null):
            moves.append((self.row + fwd, self.col))
            if self.first_move:
                moves.append((self.row + 2 * fwd, self.col))

        # basic capture
        for side in [-1, 1]:
            if self.col + side in (-1, DIM):
                continue

            piece = game[(self.row + fwd, self.col + side)]
            if not isinstance(piece, Null):
                if piece.is_white != self.is_white:
                    moves.append((self.row + fwd, self.col + side))

        return moves


class Rook(Piece):
    pass


class Bishop(Piece):
    pass


class Night(Piece):
    """ Night used in place of Knight """
    pass


class King(Piece):
    pass


class Queen(Piece):
    pass


class Null:
    """ Represents empty spaces on the chess board """

    def __init__(self):
        self.name = '--'

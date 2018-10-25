import pygame

class Piece:
    def __init__(self, team = None, name = None, range = None, moves = None):

        self.team = team
        self.range = range
        self.moves = moves

        if (team == 1):
            self.name = name + 'l'
        elif (team == -1):
            self.name = name + 'd'
        else:
            self.name = "00"


class Pawn(Piece):
    def __init__(self, team):
        moves = team * [
            [1, -1],
            [1, 0],
            [1, 1]
        ]
        Piece.__init__(self, team, "p", False, moves)


class Knight(Piece):
    def __init__(self, team):
        moves = [
            [1, 2],
            [1, -2],
            [2, 1],
            [2, -1],
            [-1, -2],
            [-1, 2],
            [-2, -1],
            [-2, 1]
        ]
        Piece.__init__(self, team, "n", False, moves)


class Bishop(Piece):
    def __init__(self, team):
        moves = [
            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1]
        ]
        Piece.__init__(self, team, "b", True, moves)


class Rook(Piece):
    def __init__(self, team):
        moves = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]
        Piece.__init__(self, team, "r", True, moves)


class Queen(Piece):
    def __init__(self, team):
        moves = [
            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1],
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]
        Piece.__init__(self, team, "q", False, moves)


class King(Piece):
    def __init__(self, team):
        moves = [
            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1],
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]
        Piece.__init__(self, team, "k", False, moves)
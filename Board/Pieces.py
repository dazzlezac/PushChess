class Piece:
    def __init__(self, team=None, name=None, moves=None):

        self.team = team
        self.moves = moves

        if team == 1:
            self.name = name + 'l'
        elif team == -1:
            self.name = name + 'd'
        else:
            self.name = '00'


class Pawn(Piece):
    def __init__(self, team):
        moves = [
            [-team*1, -team*-1],
            [-team*1, 0],
            [-team*1, -team*1]
        ]
        Piece.__init__(self, team, "p", moves)


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
        Piece.__init__(self, team, "n", moves)


class Bishop(Piece):
    def __init__(self, team):
        moves = []
        for i in range(1, 7):
            moves.extend([
                [i*1, i*1],
                [i*1, -i*1],
                [-i*1, i*1],
                [-i*1, -i*1]
            ])
        Piece.__init__(self, team, "b", moves)


class Rook(Piece):
    def __init__(self, team):
        moves = []
        for i in range(1, 7):
            moves.extend([
                [i*1, i*0],
                [i*0, i*1],
                [-i*1, i*0],
                [i*0, -i*1]
            ])
        Piece.__init__(self, team, "r", moves)


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
        Piece.__init__(self, team, "q", moves)


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
        Piece.__init__(self, team, "k", moves)


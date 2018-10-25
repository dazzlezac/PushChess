import Board.Cell as c
import Board.Pieces as p


class Board:

    # Create a map of empty cells
    def __init__(self):
        self.rows = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.Cells = {}
        for x in self.cols:
            for y in self.rows:
                self.Cells[x + y] = c.Cell()

    # Board positions are numbered as
    # a8 b8 c8 d8 e8 f8 g8 h8
    # a7 b7 c7 d7 e7 f7 g7 h7
    # a6 b6 c6 d6 e6 f6 g6 h6
    # a5 b5 c5 d5 e5 f5 g5 h5
    # a4 b4 c4 d4 e4 f4 g4 h4
    # a3 b3 c3 d3 e3 f3 g3 h3
    # a2 b2 c2 d2 e2 f2 g2 h2
    # a1 b1 c1 d1 e1 f1 g1 h1

    # Load the map from file
    def loadmap(self, filename=None):
        if filename is None:
            # White pieces (team = 1)
            self.Cells['b3'].piece = p.Pawn(1)
            self.Cells['b4'].piece = p.Pawn(1)
            self.Cells['c4'].piece = p.Pawn(1)
            self.Cells['d4'].piece = p.Pawn(1)
            self.Cells['e4'].piece = p.Pawn(1)
            self.Cells['f4'].piece = p.Pawn(1)
            self.Cells['g4'].piece = p.Pawn(1)
            self.Cells['g3'].piece = p.Pawn(1)
            self.Cells['b3'].piece = p.Pawn(1)

            self.Cells['a1'].piece = p.Knight(1)
            self.Cells['h1'].piece = p.Knight(1)

            self.Cells['b2'].piece = p.Rook(1)
            self.Cells['g2'].piece = p.Rook(1)

            self.Cells['c2'].piece = p.Bishop(1)
            self.Cells['f2'].piece = p.Bishop(1)

            self.Cells['d2'].piece = p.King(1)
            self.Cells['e2'].piece = p.Queen(1)

            # Black pieces (team = -1)
            self.Cells['b6'].piece = p.Pawn(-1)
            self.Cells['b5'].piece = p.Pawn(-1)
            self.Cells['c5'].piece = p.Pawn(-1)
            self.Cells['d5'].piece = p.Pawn(-1)
            self.Cells['e5'].piece = p.Pawn(-1)
            self.Cells['f5'].piece = p.Pawn(-1)
            self.Cells['g5'].piece = p.Pawn(-1)
            self.Cells['g6'].piece = p.Pawn(-1)
            self.Cells['b6'].piece = p.Pawn(-1)

            self.Cells['a8'].piece = p.Knight(-1)
            self.Cells['h8'].piece = p.Knight(-1)

            self.Cells['b7'].piece = p.Rook(-1)
            self.Cells['g7'].piece = p.Rook(-1)

            self.Cells['c7'].piece = p.Bishop(-1)
            self.Cells['f7'].piece = p.Bishop(-1)

            self.Cells['d7'].piece = p.King(-1)
            self.Cells['e7'].piece = p.Queen(-1)

        else:
            self.e = True
    #

    # Save the board state to external XML file
    def save(self):
        self.s = True
        #TODO

    # Load the board state from external XML file
    def load(self):
        self.l = True
        #TODO

import Board.Cell as cell
import Board.Pieces as p


class Board:

    # Create a map of empty cells
    def __init__(self):
        self.rows = ['8', '7', '6', '5', '4', '3', '2', '1']
        self.cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.Cells = {}
        for i in range(0, 8):
            for j in range(0, 8):
                c = self.cols[i]
                r = self.rows[j]
                if (i + j) % 2 == 0:
                    self.Cells[c + r] = cell.Cell('sl', i, j)
                else:
                    self.Cells[c + r] = cell.Cell('sd', i, j)

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
            pass

    # Pushes a chain of pieces
    def push(self, move, x2, y2, p1):

        # Find the piece in the cell being pushed
        c2 = self.cols[y2] + self.rows[x2]
        p2 = self.Cells[c2].piece

        # Find the position to move p2 to
        x3 = x2 + move[0]
        y3 = y2 + move[1]

        # Push p2 onto the next cell in line (if it exists)
        if p2.name is not '00':
            if (0 <= x3 < 8) and (0 <= y3 < 8):
                self.push(move, x3, y3, p2)

        # Replace the cell with the piece that moved in
        self.Cells[c2].piece = p1

    def all_threats(self, tile):
        moves = {}

        for key in self.Cells:
            print(key)

    # Checks that a movement is valid for a piece
    def valid_move(self, x1, y1, x2, y2):
        # If the destination is outside the board, invalid
        if not (0 <= x2 < 8) and (0 <= y2 < 8):
            return False

        # Calculate the move
        move = [x2 - x1, y2 - y1]

        # Find the cells
        c1 = self.cols[y1] + self.rows[x1]
        c2 = self.cols[y2] + self.rows[x2]

        # Find the pieces
        p1 = self.Cells[c1].piece
        p2 = self.Cells[c2].piece

        # Prevents moving directly onto same team
        if p1.team == p2.team:
            return False

        # Check that the move is in the moveset
        if move not in p1.moves:
            return False

        # Check pawn specific conditions
        if isinstance(p1, p.Pawn):
            n = p2.name is '00'
            m = 0 in move
            # If the square in front is blocked
            if m and not n:
                return False
            # If the diagonal is empty
            elif not m and n:
                return False

        # Check bishop specific conditions
        elif isinstance(p1, p.Bishop):
            x = move[0]
            y = move[1]
            while abs(x) > 1:
                x -= abs(x) / x
                y -= abs(y) / y
                c3 = self.cols[y1 + round(y)] + self.rows[x1 + round(x)]
                print(c3)
                if self.Cells[c3].piece.name is not '00':
                    return False
            # Updates 'move' for the pushing sequence
            move[0] = round(x)
            move[1] = round(y)

        # Check rook specific conditions
        elif isinstance(p1, p.Rook):
            # Horizontal movement impeded
            if move[0] is 0:
                y = move[1]
                print()
                while abs(y) > 1:
                    # Check 1 square closer
                    y -= abs(y) / y
                    c3 = self.cols[y1 + round(y)] + self.rows[x1]
                    print(c3)
                    if self.Cells[c3].piece.name is not '00':
                        return False
                # Update 'move' for the push sequence
                move[1] = round(y)

            # Vertical movement impeded
            else:
                x = move[0]
                print()
                while abs(x) > 1:
                    # Check 1 square closer
                    x -= abs(x) / x
                    c3 = self.cols[y1] + self.rows[x1 + round(x)]
                    print(c3)
                    if self.Cells[c3].piece.name is not '00':
                        return False
                # Update 'move' for the push sequence
                move[0] = round(x)

        # Check king specific conditions
        elif isinstance(p1, p.King):
            self.all_threats()
            pass

        self.push(move, x2, y2, p1)
        self.Cells[c1].piece = p.Piece()
        return True


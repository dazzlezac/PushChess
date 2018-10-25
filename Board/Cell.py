from Board import Pieces as p

# A single cell on the board
class Cell:

    def __init__(self, piece = p.Piece()):
        self.piece = piece

    # Moves the piece in the cell to the target cell
    def move(self, piece):

        # If the cell has a piece on it, move the piece first
        #if (self.occupied()):
        #    self.move(piece)

        # Update the piece on the cell
        self.piece = piece

    # Returns true if the cell has a piece
    def occupied(self):
        if (self.piece.name != None):
            return True
        else:
            return False




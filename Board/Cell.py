from Board import Pieces as p
import pygame

# A single cell on the board
class Cell:

    def __init__(self, colour, x, y, piece=p.Piece()):
        self.x = x
        self.y = y
        self.colour = colour
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

    def draw(self, imgs, surface):
        a = imgs[self.colour]
        b = imgs[self.piece.name]
        dest = (self.x * 100, self.y * 100)
        surface.blit(a, dest)
        surface.blit(b, dest)


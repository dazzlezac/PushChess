import pygame
import Board.Board as bd
import Board.Pieces as ps
import os
import math


def coord_convert(x, y):
    r = math.floor(y / 100)
    c = math.floor(x / 100)

    return r, c

def get_key(r, c):
    rows = ['8', '7', '6', '5', '4', '3', '2', '1']
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return cols[c] + rows[r]


def main():
    # Setup the display
    pygame.init()
    surface = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Push Chess v1.0')

    imgs = {}
    path = '/home/michael/Documents/Code/PushChess/Images/'
    imgs['sd'] = pygame.image.load(os.path.abspath(path + 'square_dark.png')).convert()
    imgs['sl'] = pygame.image.load(os.path.abspath(path + 'square_light.png')).convert()
    imgs['00'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_00.png')).convert_alpha()
    imgs['bd'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_bd.png')).convert_alpha()
    imgs['bl'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_bl.png')).convert_alpha()
    imgs['kd'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_kd.png')).convert_alpha()
    imgs['kl'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_kl.png')).convert_alpha()
    imgs['nd'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_nd.png')).convert_alpha()
    imgs['nl'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_nl.png')).convert_alpha()
    imgs['pd'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_pd.png')).convert_alpha()
    imgs['pl'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_pl.png')).convert_alpha()
    imgs['qd'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_qd.png')).convert_alpha()
    imgs['ql'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_ql.png')).convert_alpha()
    imgs['rd'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_rd.png')).convert_alpha()
    imgs['rl'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_rl.png')).convert_alpha()

    for img in imgs:
        imgs[img] = pygame.transform.scale(imgs[img], (100, 100))

    # Construct the board
    board = bd.Board()
    board.loadmap()

    for m in range(0, 8):
        for n in range(0, 8):
            board.Cells[get_key(n, m)].draw(imgs, surface)

    empty = ps.Piece()
    turn = 0

    while True:
        pygame.display.update()
        pygame.display.flip()

        # Check if anything happened on the surface
        event = pygame.event.poll()

        # Quit the game if QUIT is initiated
        if event.type == pygame.QUIT:
            pygame.quit()
            break

        # Check which square the player clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x1, y1 = coord_convert(x, y)
            s1 = get_key(x1, y1)
            p = board.Cells[s1].piece

        # Check which square the player released on
        elif event.type == pygame.MOUSEBUTTONUP:
            # If it's not the clicked pieces turn
            if p.team == 1 and turn % 2 is not 0:
                print('Wrong team')
                continue
            elif p.team == -1 and turn % 2 is not 1:
                print('Wrong team')
                continue

            x, y = pygame.mouse.get_pos()
            x2, y2 = coord_convert(x, y)
            s2 = get_key(x2, y2)
            if board.valid_move(x1, y1, x2, y2):

                # Draw the changes
                for m in range(0, 8):
                    for n in range(0, 8):
                        board.Cells[get_key(n, m)].draw(imgs, surface)

                turn += 1
            else:
                print('Invalid move')


###########################################

main()

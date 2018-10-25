import pygame
import Board.Board as bd
import os

# Setup the display
pygame.init()
surface = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Push Chess v0.1')
tile = pygame.Surface((100, 100)).convert()

imgs = {}
path = '/home/michael/Documents/Code/PushChess/Images/'
imgs['sd'] = pygame.image.load(os.path.abspath(path + 'square_dark.png')).convert()
imgs['sl'] = pygame.image.load(os.path.abspath(path + 'square_light.png')).convert()
imgs['00'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_00.png')).convert_alpha()
imgs['bd'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_bd.png')).convert()
imgs['bl'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_bl.png')).convert()
imgs['kd'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_kd.png')).convert()
imgs['kl'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_kl.png')).convert()
imgs['nd'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_nd.png')).convert()
imgs['nl'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_nl.png')).convert()
imgs['pd'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_pd.png')).convert()
imgs['pl'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_pl.png')).convert()
imgs['qd'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_qd.png')).convert()
imgs['ql'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_ql.png')).convert()
imgs['rd'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_rd.png')).convert()
imgs['rl'] = pygame.image.load(os.path.abspath(path + 'Chess_tile_rl.png')).convert()

for img in imgs:
    imgs[img] = pygame.transform.scale(imgs[img], (100, 100))

# Construct the board
board = bd.Board()
board.loadmap()

rect = pygame.Rect(0, 0, 100, 100)

i = 0
for x in board.cols:
    j = 0
    for y in board.rows:
        if (i + j) % 2 == 0:
            surface.blit(imgs['sl'], (i * 100, j * 100))
        else:
            surface.blit(imgs['sd'], (i * 100, j * 100))

        n = board.Cells[x + y].piece.name
        print(n)
        surface.blit(imgs[n], (i*100, j*100))
        pygame.display.flip()
        j += 1
    i += 1

pygame.display.flip()

while True:

    # Quit the game if QUIT is initiated
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        break


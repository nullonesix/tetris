import random
import pygame
import time

pygame.init()

board = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
]

pieces = [
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    [
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 0]
    ],
    [
        [1, 1],
        [1, 1]
    ],
    [
        [0, 1, 1],
        [1, 1, 0],
        [0, 0, 0]
    ],
    [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ],
    [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ],
    [
        [0, 1, 1],
        [0, 1, 0],
        [0, 1, 0]
    ]
]

w = 800
h = 600

surface = pygame.display.set_mode((w, h))

def draw_board():
    s = 20 # for sidelength of each tile
    g = 2 # for gaps between tiles
    hs = w//2 - s*len(board[0])//2 # for horizontal shift of board on surface
    vs = h//2 - s*len(board)//2 # for vertical shift of board on surface
    for i in range(len(board)):
        for j in range(len(board[0])):
            pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(hs+s*j, vs+s*i, s, s))
            if board[i][j] == 1:
                pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(hs+s*j, vs+s*i, s-g, s-g))
    pygame.display.flip()

def piece_generator():
    while True:
        random.shuffle(pieces)
        for piece in pieces:
            yield piece

generator = piece_generator()

def collision(piece, x, y):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if board[x+i][y+j] > 1:
                return True
    return False

def place_piece(piece, x, y):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            board[x+i][y+j] += piece[i][j]

def remove_piece(piece, x, y):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            board[x+i][y+j] -= piece[i][j]

def move_left(piece, x, y):
    remove_piece(piece, x, y)
    place_piece(piece, x, y-1)
    return piece, x, y-1

def move_right(piece, x, y):
    remove_piece(piece, x, y)
    place_piece(piece, x, y+1)
    return piece, x, y+1

def move_rotate(piece, x, y):
    rotated_piece = list(zip(*piece[::-1]))
    remove_piece(piece, x, y)
    place_piece(rotated_piece, x, y)
    return rotated_piece, x, y

def gravity(piece, x, y):
    remove_piece(piece, x, y)
    place_piece(piece, x+1, y)
    return piece, x+1, y

def clear_line():
    for i in range(len(board)-4, -1, -1):
        line_saturated = True
        for j in range(len(board[0])-4, 2, -1):
            if board[i][j] == 0:
                line_saturated = False
        if line_saturated:
            for k in range(i, -1, -1):
                for l in range(len(board[0])-4, 2, -1):
                    board[k][l] = board[k-1][l]

def process_input(piece, x, y):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                piece, x, y = move_left(piece, x, y)
            if event.key == pygame.K_RIGHT:
                piece, x, y = move_right(piece, x, y)
            if event.key == pygame.K_UP:
                piece, x, y = move_rotate(piece, x, y)
            if event.key == pygame.K_DOWN:
                piece, x, y = gravity(piece, x, y)
            if event.key == pygame.K_SPACE:
                while not collision(piece, x, y):
                    piece, x, y = gravity(piece, x, y)
                remove_piece(piece, x, y)
                place_piece(piece, x-1, y)
                piece, x, y = piece, x-1, y
            if event.key == pygame.K_q:
                pygame.quit()
    return piece, x, y

piece = next(generator)
x = 0
y = len(board[0])//2 - len(piece)//2
place_piece(piece, x, y)
t0 = time.time()

while True:
    piece2, x2, y2 = process_input(piece, x, y)
    if collision(piece2, x2, y2):
        remove_piece(piece2, x2, y2) # undo the move if there's a collision
        place_piece(piece, x, y)
    else:
        piece, x, y = piece2, x2, y2
    clear_line()
    if time.time() - t0 > 1:
        piece2, x2, y2 = gravity(piece, x, y)
        if collision(piece2, x2, y2):
            remove_piece(piece2, x2, y2) # undo gravity if there's a collision
            place_piece(piece, x, y) # place the piece to where it was
            piece, x, y = next(generator), 0, len(board[0])//2 - len(piece)//2 # get a new piece
            place_piece(piece, x, y) # and place it at the top of the board
        else:
            piece, x, y = piece2, x2, y2
        t0 = time.time()
    draw_board()

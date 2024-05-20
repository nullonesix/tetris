import random
import pygame
import time
import copy
import sys

pygame.init()

board_init = [
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
    [0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
]

pieces = [
    [
        [0, 11, 0],
        [11, 11, 11],
        [0, 0, 0]
    ],
    [
        [12, 12, 0],
        [0, 12, 12],
        [0, 0, 0]
    ],
    [
        [13, 13],
        [13, 13]
    ],
    [
        [0, 14, 14],
        [14, 14, 0],
        [0, 0, 0]
    ],
    [
        [0, 0, 0, 0],
        [15, 15, 15, 15],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ],
    [
        [16, 16, 0],
        [0, 16, 0],
        [0, 16, 0]
    ],
    [
        [0, 17, 17],
        [0, 17, 0],
        [0, 17, 0]
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
            if board[i][j] == 10:
                pygame.draw.rect(surface, (155, 155, 155), pygame.Rect(hs+s*j, vs+s*i, s-g, s-g))
            if board[i][j] == 11:
                pygame.draw.rect(surface, (255, 0, 255), pygame.Rect(hs+s*j, vs+s*i, s-g, s-g))
            if board[i][j] == 12:
                pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(hs+s*j, vs+s*i, s-g, s-g))
            if board[i][j] == 13:
                pygame.draw.rect(surface, (255, 255, 0), pygame.Rect(hs+s*j, vs+s*i, s-g, s-g))
            if board[i][j] == 14:
                pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(hs+s*j, vs+s*i, s-g, s-g))
            if board[i][j] == 15:
                pygame.draw.rect(surface, (0, 155, 255), pygame.Rect(hs+s*j, vs+s*i, s-g, s-g))
            if board[i][j] == 16:
                pygame.draw.rect(surface, (255, 155, 0), pygame.Rect(hs+s*j, vs+s*i, s-g, s-g))
            if board[i][j] == 17:
                pygame.draw.rect(surface, (0, 0, 255), pygame.Rect(hs+s*j, vs+s*i, s-g, s-g))
            if not board[i][j] in [10, 11, 12, 13, 14, 15, 16, 17, 0]:
                # pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(hs+s*j, vs+s*i, s-g, s-g))
                pygame.draw.rect(surface, (235, 235, 235), pygame.Rect(hs+s*j, vs+s*i, s-g, s-g))
    pygame.display.flip()

def piece_generator():
    while True:
        random.shuffle(pieces)
        for piece in pieces:
            yield piece

def collision():
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if board[x+i][y+j] >= 20:
                return True
    return False

def place_piece():
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            board[x+i][y+j] += piece[i][j]

def remove_piece():
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            board[x+i][y+j] -= piece[i][j]

def clear_line():
    for i in range(len(board)-4, -1, -1):
        line_saturated = True
        for j in range(len(board[0])-4, 2, -1):
            if board[i][j] == 0:
                line_saturated = False
        if line_saturated:
            print('line clear')
            for k in range(i, -1, -1):
                for l in range(len(board[0])-4, 2, -1):
                    board[k][l] = board[k-1][l]

def move_left():
    global piece, x, y
    remove_piece()
    y -= 1
    place_piece()
    if collision():
        remove_piece()
        y += 1
        place_piece()

def move_right():
    global piece, x, y
    remove_piece()
    y += 1
    place_piece()
    if collision():
        remove_piece()
        y -= 1
        place_piece()

def move_rotate():
    global piece, x, y
    remove_piece()
    piece = list(zip(*piece[::-1]))
    place_piece()
    if collision():
        remove_piece()
        for _ in range(3):
            piece = list(zip(*piece[::-1]))
        place_piece()

def move_down():
    global piece, x, y
    remove_piece()
    x += 1
    place_piece()
    if collision():
        remove_piece()
        x -= 1
        place_piece()

def move_drop():
    global piece, x, y
    while not collision():
        remove_piece()
        x += 1
        place_piece()
    remove_piece()
    x -= 1
    place_piece()

def process_input():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
            if event.key == pygame.K_RIGHT:
                move_right()
            if event.key == pygame.K_UP:
                move_rotate()
            if event.key == pygame.K_DOWN:
                move_down()
            if event.key == pygame.K_SPACE:
                move_drop()
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

def gravity():
    global piece, x, y, generator, board, t0
    if time.time() - t0 > 1:
        t0 = time.time()
        remove_piece()
        x += 1
        place_piece()
        if collision():
            remove_piece()
            x -= 1
            if x <= x_init:
                print('game over')
                board = copy.deepcopy(board_init)
                generator = piece_generator()
                piece, x, y = next(generator), x_init, y_init
                place_piece()
                return 
            place_piece()
            piece, x, y = next(generator), x_init, y_init 
            place_piece()

generator = piece_generator()
board = copy.deepcopy(board_init)
piece = next(generator)
x_init = 0
y_init = len(board[0])//2 - len(piece)//2
x = x_init
y = y_init
place_piece()
t0 = time.time()

while True:
    process_input()
    gravity()
    clear_line()
    draw_board()

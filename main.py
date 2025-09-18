import pygame
import random
from pprint import PrettyPrinter
printer = PrettyPrinter()

pygame.init()

WIDTH, HEIGHT = 700, 400


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

BG_COLOR = "white"

ROWS, COLS = 10, 10
MINES = 15

NUM_FONT = pygame.font.SysFont("comicsans", 20)
NUM_COLORS = {
    1: (0, 0, 255),
    2: (0, 128, 0),
    3: (255, 0, 0),
    4: (0, 0, 128),
    5: (128, 0, 0),
    6: (64, 224, 208),
    7: (0, 0, 0),
    8: (128, 128, 128)
}
RECT_COLOR = (200, 200, 200)

def get_neighbors(row, col, rows, cols):
    neighbors = []
    
    if row > 0:
        neighbors.append((row - 1 , col ))
    if row < rows - 1:
        neighbors.append((row + 1 , col))
    if col > 0:
        neighbors.append((row , col -1 ))
    if col < cols - 1:
        neighbors.append((row , col +1 ))
    
    if row > 0 and col > 0:
        neighbors.append((row - 1, col - 1))
    if row < rows - 1 and col < cols - 1:
        neighbors.append((row + 1, col + 1))
    if row < rows - 1 and col > 0:
        neighbors.append((row + 1, col - 1))
    if row > 0 and col < cols - 1:
        neighbors.append((row - 1, col + 1))

    print
    return neighbors
    

def create_minefield(rows, cols, mines):
    field = [[ 0 for _ in range(cols)] for _ in range(rows)]
    mine_positions = set()
    


    while len(mine_positions) < mines:
        row = random.randrange(0, rows)
        col = random.randrange(0, cols)
        pos = row, col 


        if pos in mine_positions:
            continue
        mine_positions.add(pos)
        field[row][col]= -1

    for mine in mine_positions:
        neighbors = get_neighbors(*mine, rows, cols)
        for r, c in neighbors:
            if field[r][c] != -1:
                field[r][c] += 1
    return field

def draw(win, field, cover_field):
    win.fill(BG_COLOR)

    size = WIDTH // ROWS
    for i, row in enumerate(field):
        y = size * i
        for j, value in enumerate(row):
            x = size * j
            pygame.draw.rect(win, RECT_COLOR, (x,y,size,size))
            pygame.draw.rect(win, "black", (x,y,size,size), 2)

            if value > 0:
                text = NUM_FONT.render(str(value), 1, NUM_COLORS[value])
                win.blit(text, (x,y))
                win.blit(text, (x + (size/2 - text.get_width()/2), y + (size/2 - text.get_height()/2)))

    pygame.display.update()

def main(win):
    run = True
    cover_field = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    field = create_minefield(ROWS, COLS, MINES)
    printer.pprint(field)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(win, field, cover_field)

    pygame.quit()

    
if __name__ == "__main__":
    main(win)
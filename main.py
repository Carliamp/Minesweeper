# main  

import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

BG_COLOR = "white"

def draw(win):
    win.fill(BG_COLOR)
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(win)

    pygame.quit()

    
if __name__ == "__main__":
    main(win)
import pygame
import time
import os
import blackjack_oop as bj

pygame.font.init()

# CONSTANTS

# Display
WIDTH = 750
HEIGHT = 750
BACKGROUND = (53, 173, 28)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack Game")

# Images
HIT_IMG = pygame.transform.scale(pygame.image.load(os.path.join("images", "buttons", "button_hit.png")), (100, 45))
STAND_IMG = pygame.transform.scale(pygame.image.load(os.path.join("images", "buttons", "button_stand.png")), (100, 45))
PLAY_IMG = pygame.transform.scale(pygame.image.load(os.path.join("images", "buttons", "button_play.png")), (100, 45))
RED_CHIP_IMG = pygame.transform.scale(pygame.image.load(os.path.join("images", "chips", "red_chip.png")), (100, 75))


def main():
    FPS = 60
    run = True
    clock = pygame.time.Clock()
    chips = 1000
    main_font = pygame.font.SysFont("comicsans", 50)

    def redraw_window():
        # Draw the background
        WIN.fill(BACKGROUND)

        # Draw the score text
        chips_label = main_font.render(f"Chips: {chips}", 1, (0, 0, 0))
        WIN.blit(chips_label, (WIDTH - chips_label.get_width() - 10, 10))

        # Draw the buttons
        WIN.blit(HIT_IMG, (WIDTH - HIT_IMG.get_width() - 50, HEIGHT - HIT_IMG.get_height() - 50))
        WIN.blit(STAND_IMG, (WIDTH - STAND_IMG.get_width() - 200, HEIGHT - STAND_IMG.get_height() - 50))
        WIN.blit(PLAY_IMG, (WIDTH - PLAY_IMG.get_width() - 350, HEIGHT - PLAY_IMG.get_height() - 50))
        WIN.blit(RED_CHIP_IMG, (50, HEIGHT - RED_CHIP_IMG.get_height() - 50))

        # Update the display
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HIT_IMG.get_rect().collidepoint(mouse):
                    print("mouse is over 'newGameButton'")


print(HIT_IMG.get_rect(), PLAY_IMG.get_rect())
# main()

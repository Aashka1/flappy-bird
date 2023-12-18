import pygame
import sys
from pygame.locals import *

def wallpaper():
    # Initialize Pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 1350, 650
    WHITE = (255, 255, 255)

    # Create the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird Home Screen")

    # Load background image (replace with your own image path)
    background = pygame.image.load("bp2.png").convert_alpha()
    play_button = pygame.image.load("play.png").convert_alpha()

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                # Check if the mouse click is within the play button area
                mouse_x, mouse_y = pygame.mouse.get_pos()
                play_button_rect = play_button.get_rect()
                play_button_rect.center = (650, 450)
                
                if play_button_rect.collidepoint(mouse_x, mouse_y):
                    print("Game start")
        
        # Blit the background at (0, 0) to cover the entire screen
        screen.blit(background, (50, 0))
        
        # Display the play button in the center of the screen
        play_button_rect = play_button.get_rect()
        play_button_rect.center = (650, 450)
        screen.blit(play_button, play_button_rect)
        
        pygame.display.update()
        
        # Cap the frame rate to 60 FPS
        clock.tick(60)

def main():
    wallpaper()

if __name__ == "__main__":
    main()

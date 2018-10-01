import sys
import pygame
#from ship import Ship
from settings import Settings


def run_game():
       # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

#    ship = Ship(screen)

    bg_color=(230,230,230)

       # Start the main loop for the game.
    while True:

           # Watch for keyboard and mouse events.
     for event in pygame.event.get():
       if event.type == pygame.QUIT:
         sys.exit()

         screen_fill(ai_settings.bg_color)
         ship.blitme()

           # Make the most recently drawn screen visible.
         pygame.display.flip()

run_game()

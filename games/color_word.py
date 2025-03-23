import pygame
import sys

pygame.init()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
SPEED = 5
SCORE = 0

FPS = 120
FramePerSec = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

base_font = pygame.font.Font(None, 32)
font = pygame.font.SysFont("Verdana", 60)
user_text = ''

input_rect = pygame.Rect(200, 200, 300, 32)
color_active = pygame.Color('lightgray')
color_passive = pygame.Color('chartreuse4')
color = color_passive

active = False

while True:
    for event in pygame.event.get():

        # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

        if event.type == pygame.K_KP_ENTER:
            user_text += event.unicode

    # it will set background color of screen
    SCREEN.fill((255, 255, 255))

    if active:
        color = color_active
    else:
        color = color_passive

    scores = base_font.render(str(SCORE), True, BLACK)
    SCREEN.blit(scores, (10, 10))

    # Input text section
    pygame.draw.rect(SCREEN, color, input_rect, border_radius=3)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    SCREEN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(100, text_surface.get_width() + 10)

    # Start button
    start_button = pygame.draw.rect(SCREEN, GREEN, input_rect, border_radius=4)
    start_button.x = 0
    start_button.y = 0
    # SCREEN.blit(start_button, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    # display.flip() will update only a portion of the screen to updated, not full area
    pygame.display.flip()
    # pygame.display.update()
    FramePerSec.tick(FPS)
"""
Instructions: navigate the levels to fill all blocks using a single path to win!
"""
import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 120
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
SPEED = 5
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN.fill(WHITE)
pygame.display.set_caption("Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    SCREEN.blit(scores, (10, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        SCREEN.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    # if pygame.sprite.spritecollideany(P1, enemies):
    #     pygame.mixer.Sound('crash.wav').play()
    #     time.sleep(0.5)
    #
    #     SCREEN.fill(RED)
    #     SCREEN.blit(game_over, (30, 250))
    #
    #     pygame.display.update()
    #     for entity in all_sprites:
    #         entity.kill()
    #     time.sleep(2)
    #     pygame.quit()
    #     sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
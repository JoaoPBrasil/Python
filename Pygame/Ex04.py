import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Colisão de Retângulos")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

class Player:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update_position(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        self.rect.center = (mouse_x, mouse_y)

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

def generate_random_rectangles(num):
    rectangles = []
    for _ in range(num):
        width = random.randint(30, 100)
        height = random.randint(30, 100)
        x = random.randint(0, SCREEN_WIDTH - width)
        y = random.randint(0, SCREEN_HEIGHT - height)
        rectangles.append(pygame.Rect(x, y, width, height))
    return rectangles

def game_loop():
    clock = pygame.time.Clock()
    running = True
    player = Player()
    rectangles = generate_random_rectangles(10)
    score = 0

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update_position()

        for rect in rectangles[:]:
            if player.rect.colliderect(rect):
                rectangles.remove(rect)
                score += 1

        for rect in rectangles:
            pygame.draw.rect(screen, RED, rect)

        player.draw()

        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Pontuação: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            player = Player()
            rectangles = generate_random_rectangles(10)
            score = 0

        clock.tick(60)

    pygame.quit()

game_loop()

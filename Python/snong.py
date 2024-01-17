import pygame
from objects import Ball, Paddle, Snake

pygame.init()
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Snong")
clock = pygame.time.Clock()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.fill("black")


        clock.tick(60)  # limits FPS to 60

if __name__ == "__main__":
    main()
    pygame.quit()
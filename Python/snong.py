# Pong code inspired by/derived from: https://www.geeksforgeeks.org/create-a-pong-game-in-python-pygame/#

import pygame
from objects import Ball, Paddle, Snake

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PIXEL_WIDTH = 20
PADDLE_HEIGHT = 100

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snong")

clock = pygame.time.Clock()

def main():
    running = True

    left_paddle = Paddle(window, 20, (SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2), 
                         PIXEL_WIDTH, PADDLE_HEIGHT, 10, WHITE)
    right_paddle = Paddle(window, SCREEN_WIDTH - (PIXEL_WIDTH * 2), 
                          (SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2), PIXEL_WIDTH, PADDLE_HEIGHT, 10, WHITE)

    left_y_dir = 0
    right_y_dir = 0

    ball = Ball(window, (SCREEN_WIDTH/2 - PIXEL_WIDTH/2), 
                (SCREEN_HEIGHT/2 - PIXEL_WIDTH/2), PIXEL_WIDTH, 5, WHITE)

    while running:
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    right_y_dir = -1
                if event.key == pygame.K_DOWN:
                    right_y_dir = 1
                if event.key == pygame.K_w:
                    left_y_dir = -1
                if event.key == pygame.K_s:
                    left_y_dir = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    right_y_dir = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    left_y_dir = 0

        if pygame.Rect.colliderect(left_paddle.getRect(), ball.getRect()):
            ball.hit()
        elif pygame.Rect.colliderect(right_paddle.getRect(), ball.getRect()):
            ball.hit()
        
        left_paddle.update(left_y_dir)
        right_paddle.update(right_y_dir)
        status = ball.update()

        if status == 0:
            left_paddle.reset()
            right_paddle.reset()
            ball.reset()

        left_paddle.display()
        right_paddle.display()
        ball.display()

        pygame.display.update()

        clock.tick(60)  # limits FPS to 60

if __name__ == "__main__":
    main()
    pygame.quit()
import pygame
import random
import time

class Ball:
    def __init__(self, window, x, y, size, speed, color):
        self.window = window
        self.posx = x
        self.posy = y
        self.width = size   # Both width and height are the same since it is a square
        self.height = size
        self.speed = speed
        self.color = color
        self.x_dir = random.choice([-1, 1])
        self.y_dir = random.choice([-1, 1])
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)

    def display(self):
        pygame.draw.rect(self.window, self.color, self.rect)
        
    def update(self):
        self.posx += self.speed * self.x_dir
        self.posy += self.speed * self.y_dir

        if self.posx <= 0 or self.posx >= (self.window.get_width() - self.width):
            return 0 # Returns 0  to signal end of round
        elif self.posy <= 0 or self.posy >= (self.window.get_height() - self.height):
            self.y_dir *= -1

        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)

        return 1 # Returns 1 to signal the ball is still in play

    def hit(self):
        self.x_dir *= -1

    def reset(self):
        w = self.window.get_width()
        h = self.window.get_height()
        
        self.posx = w//2
        self.posy = h//2
        self.x_dir = random.choice([-1, 1])
        self.y_dir = random.choice([-1, 1])
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        time.sleep(2)

    def getRect(self):
        return self.rect
    
class Paddle:
    def __init__(self, window, x, y, width, height, speed, color):
        self.window = window
        self.posx = x
        self.posy = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)

    def display(self):
        pygame.draw.rect(self.window, self.color, self.rect)
        
    def update(self, y_dir):
        self.posy += (self.speed * y_dir)
        
        if self.posy <= 0:
            self.posy = 0
        elif (self.posy + self.height) >= self.window.get_height():
            self.posy = self.window.get_height() - self.height

        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)

    def reset(self):
        h = self.window.get_height()
        self.posy = h//2
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)

    def getRect(self):
        return self.rect

class Snake:
    def __init__():
        return
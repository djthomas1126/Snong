import pygame

pygame.init()
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Snong")
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill("black")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on window
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
import pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            k = pygame.key.name(event.key)
            print(k)
    pygame.display.update()
    clock.tick(60)
pygame.quit()

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
    x, y = pygame.mouse.get_pos()
    screen.fill("black")
    pygame.draw.circle(screen, "blue", (x, y), 20)
    pygame.display.update()
    clock.tick(60)
pygame.quit()

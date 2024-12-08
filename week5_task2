import pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
x, y = 250, 250
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5
    screen.fill("black")
    pygame.draw.circle(screen, "blue", (x, y), 40)
    pygame.display.update()
    clock.tick(60)
pygame.quit()

import pygame
import random
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
radius = 40
x, y = 250, 250
colors = ["green", "pink", "red", "blue", "yellow"]
color = "blue"
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
    if keys[pygame.K_EQUALS]:
        radius += 5
    if keys[pygame.K_MINUS]:
        radius -= 5
    if any(keys) and not keys[pygame.K_MINUS] and not keys[pygame.K_EQUALS]\
            and not keys[pygame.K_DOWN] and not keys[pygame.K_UP]\
            and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        color = random.choice(colors)
    screen.fill("black")
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.update()
    clock.tick(60)
pygame.quit()

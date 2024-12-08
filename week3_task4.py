import pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
mysurface = pygame.Surface(size)
mysurface.fill("yellow")
length = 20
x = 0
y = 0
color = (0, 255, 0)
clock = pygame.time.Clock()
running = True
move_down = True
radius = 90
w = 0
ye = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    if move_down:
        if x < width - length and y < height - length:
            x += 5
            y += 5
        else:
            move_down = False
            w = 0
            radius -= 30
    else:
        if x > length and y > length:
            x -= 5
            y -= 5
        else:
            move_down = True
            w = 1
            if radius <= 0:
                ye = True
    pygame.draw.rect(screen, color, (x, y, length, length), w)
    pygame.draw.circle(screen, "red", (400, 100), radius)
    if ye:
        screen.blit(mysurface, (0, 0))
    pygame.display.update()
    clock.tick(40)
pygame.quit()

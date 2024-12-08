import pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
pos = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pos.append((mouse_x, mouse_y))
    screen.fill("white")
    for i in pos:
        pygame.draw.circle(screen, "red", i, 10)
    pygame.display.update()
    clock.tick(60)
pygame.quit()

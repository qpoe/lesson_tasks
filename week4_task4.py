import pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
rect_width, rect_height = 50, 50
x, y = 200, 200
dragging = False
changedx, changedy = 0, 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            if x <= mousex <= x + rect_width and y <= mousey <= y + rect_height:
                dragging = True
                changedx = x - mousex
                changedy = y - mousey
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mousex, mousey = pygame.mouse.get_pos()
                x = mousex + changedx
                y = mousey + changedy
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
    screen.fill("black")
    pygame.draw.rect(screen, "red", (x, y, rect_width, rect_height))
    pygame.display.update()
    clock.tick(60)
pygame.quit()

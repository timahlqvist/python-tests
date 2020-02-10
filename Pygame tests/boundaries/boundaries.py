import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Boundaries")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(40)

    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and x > vel:
        x -= vel
    if key[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if key[pygame.K_UP] and y > vel:
        y -= vel
    if key[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    window.fill((0, 0, 0))

pygame.quit()
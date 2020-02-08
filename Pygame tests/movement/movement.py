import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Movement")

x = 50
y = 50
width = 40
height = 70
vel = 5

run = True

while run:
    pygame.time.delay(25)

    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    window.fill((0, 0, 0))


pygame.quit()
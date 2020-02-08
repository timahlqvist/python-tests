import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Draw")

x = 50
y = 50
width = 40
height = 40

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

    
pygame.quit()
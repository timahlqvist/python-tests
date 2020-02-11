# Test file for learning jumping in Pygame

# - up / left
# + down / right


import pygame
pygame.init()

# Window configuration
windowSize = 500

window = pygame.display.set_mode((windowSize, windowSize))
pygame.display.set_caption("Jumping")

# Properties for the player
x = 50
y = 400
width = 30
height = 50
vel = 8

isJumping = False   # Checks if the player is jumping
jumpCount = 10

run = True

while run:
    pygame.time.delay(50)
    key = pygame.key.get_pressed()

    pygame.draw.rect(window, (0, 0, 255), (x, y, width, height))

    if key[pygame.K_LEFT] and x > vel:
        x -= vel
    if key[pygame.K_RIGHT] and x < windowSize - vel - width:
        x += vel

    # JUMPING
    if key[pygame.K_SPACE]:
        isJumping = True

    if isJumping:   # Checks if the player is jumping
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:   # If the jumpCount is a negative number
                neg = -1
            y -= (jumpCount ** 2) / 2 * neg  # Moving the player up by the value of the jumpCount variable to the power of two divided by two  (multiplied with 0.5) multiplied with the value of neg.
            jumpCount -= 1  # Making the player slowly moving down
        else:   # The jump is concluded
            isJumping = False   # Variable reset
            jumpCount = 10      # Variable reset
        
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    window.fill((0, 0, 0))

pygame.quit()
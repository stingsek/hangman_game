import pygame
import os

# initializing
pygame.init()

## set up display

# dimensions
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH,HEIGHT))

# name of the window
pygame.display.set_caption("Hangman game")


## game variables
hangman_status = 0
# colors
WHITE = (255,255,255)


## load images
images = []
for i in range(7):
    image = pygame.image.load("images/" + "hangman" + str(i) + ".png")
    images.append(image)

## set up game loop 
# loop will run at this speed
FPS = 60
clock = pygame.time.Clock()

# loop controller
run = True

while run:
    # while loop runs with FPS speed
    clock.tick(FPS)

    window.fill(WHITE)

    # drawing image
    window.blit(images[hangman_status],(150,100))

    #update the display
    pygame.display.update()

    # loop through event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     print(pos)
    
# closing the window
pygame.quit()
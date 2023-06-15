import pygame
import os
import string

# initializing
pygame.init()


#def set_up_display()

# dimensions
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH,HEIGHT))

# name of the window
pygame.display.set_caption("Hangman game")


## game variables

hangman_status = 0

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# button variables
RADIUS = 20
GAP = 15
LINE_THICKNESS = 3
LETTERS_PER_LINE = 13
LETTERS_COUNT = 26
letters = []
start_x = round((WIDTH - ((GAP + 2 * RADIUS) * LETTERS_PER_LINE)) / 2)
start_y = 400

for i, letter in zip(range(LETTERS_COUNT), string.ascii_uppercase):
    x = start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (i % LETTERS_PER_LINE))
    y = start_y + ((i // LETTERS_PER_LINE) * (GAP + RADIUS * 2))
    letters.append([x, y, letter, True])

# fonts
FONT_SIZE = 40
LETTER_FONT = pygame.font.SysFont('comicsans', FONT_SIZE)

## load images
HANGMAN_IMAGE_X = 150
HANGMAN_IMAGE_Y = 100
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

def draw():
    window.fill(WHITE)
    window.blit(images[hangman_status],(HANGMAN_IMAGE_X,HANGMAN_IMAGE_Y))
    #draw buttons

    for letter in letters:
        x, y, l, v  = letter
        if v:
            pygame.draw.circle(window, BLACK, (x, y), RADIUS, LINE_THICKNESS)
            #text rendering
            text = LETTER_FONT.render(l, 1, BLACK)
            window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))


def is_letter_clicked(l_x,l_y,m_x,m_y):
    return (m_x - l_x) ** 2 + (m_y - l_y) ** 2 <= (RADIUS ** 2) + LINE_THICKNESS 


while run:
    # while loop runs with FPS speed
    clock.tick(FPS)
    # drawing image
    draw()

    #update the display
    pygame.display.update()

    # loop through event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                l_x, l_y, l, visible = letter
                if visible:
                    if is_letter_clicked(l_x,l_y,m_x,m_y):
                        letter[3] = False
    
# closing the window
pygame.quit()
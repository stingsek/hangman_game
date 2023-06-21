import pygame


# HANGMAN IMAGE COORDINATES
HANGMAN_IMAGE_X = 300
HANGMAN_IMAGE_Y = 100


class HangmanManager:

    def __init__(self):
        self.hangman_images = []
        self.hangman_status = 0


    def load_hangman_images(self,dir_path):
        for i in range(7):
            image = pygame.image.load(dir_path + str(i) + ".png")
            self.hangman_images.append(image)
        return self.hangman_images
    
    def is_hangman_alive(self):
        return self.hangman_status < (len(self.hangman_images) - 1)

    def draw_hangman(self, screen):
        screen.blit(self.hangman_images[self.hangman_status],(HANGMAN_IMAGE_X,HANGMAN_IMAGE_Y))
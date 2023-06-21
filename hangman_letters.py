import string
import pygame

# LETTERS DIMENSIONS AND ARRANGEMENT
RADIUS = 20
GAP = 15
LINE_THICKNESS = 3
LETTERS_PER_LINE = 13
LETTERS_COUNT = 26
START_Y_OFFSET = 100


class LetterManager:
    def __init__(self, screen):
        self.start_x = round((screen.get_size()[0] - ((GAP + 2 * RADIUS) * LETTERS_PER_LINE)) / 2)
        self.start_y = screen.get_size()[1] - START_Y_OFFSET

    @staticmethod
    def is_letter_clicked(l_x, l_y, m_x, m_y):
        # check whether the click is inside the letter circle
        return (m_x - l_x) ** 2 + (m_y - l_y) ** 2 <= (RADIUS ** 2) + LINE_THICKNESS

    def get_ascii_letters(self):
        letters = []
        for i, letter in zip(range(LETTERS_COUNT), string.ascii_uppercase):
            x = self.start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (i % LETTERS_PER_LINE))
            y = self.start_y + ((i // LETTERS_PER_LINE) * (GAP + RADIUS * 2))
            letters.append([x, y, letter, True])
        return letters
    
    @staticmethod
    def draw_letters(screen, letters, color, font):
        for letter in letters:
            x, y, l, visible  = letter
            if visible:
                pygame.draw.circle(screen, color, (x, y), RADIUS, LINE_THICKNESS)
                text = font.render(l, 1, color)
                screen.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

class FontManager:
    @staticmethod
    def get_font(size, font_path='fonts/font.ttf'):
        return pygame.font.Font(font_path, size)
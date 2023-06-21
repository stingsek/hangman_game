import random

# WORD DRAW COORDINATES
WORD_Y = 400
WORD_X = 50

# DIFFICULTY | LENGTH
HARD_MAX = 20
MEDIUM_MAX = 12
EASY_MAX = 5

class WordManager:
    def __init__(self, screen):
        self.guessed_letters = [" "]
        self.words = []
        self.word_min_length = 0
        self.word_max_length = HARD_MAX

    def update_guessed_letters(self, letter):
        self.guessed_letters.append(letter)
    
    def reset(self):
        self.guessed_letters = [" "]

    def set_word_difficulty(self,lvl):
        if lvl == "easy":
            self.word_max_length = EASY_MAX
        if lvl == "medium":
            self.word_min_length = EASY_MAX
            self.word_max_length = MEDIUM_MAX
        if lvl == "hard":
            self.word_min_length = MEDIUM_MAX
            self.word_max_length = HARD_MAX
    
    def pick_random_word(self):
        words_with_limits = [word for word in self.words if self.word_min_length <= len(word) <= self.word_max_length]
        return random.choice(words_with_limits) if words_with_limits else random.choice(self.words)

    
    def is_word_in_guessed_letters(self, word):
        for ltr in word:
            if ltr not in self.guessed_letters:
                return False
        else:
            return True

    @staticmethod
    def draw_word(screen, word, guessed, text_color, font):
        display_word = ""
        for letter in word:
            if letter in guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
    
        text = font.render(display_word, 1, text_color)
        text_rect = text.get_rect(center=(400,400))
        screen.blit(text,text_rect)

    




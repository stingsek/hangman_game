import random



class WordManager:
    def __init__(self, screen):
        # self.start_x = round((screen.get_size()[0] - ((GAP + 2 * RADIUS) * LETTERS_PER_LINE)) / 2)
        # self.start_y = screen.get_size()[1] - START_Y_OFFSET
        self.guessed_letters = []
        self.words = []
        self.picked_word_length = 0
        self.errors = 0
        self.word_min_length = 0
        self.word_max_length = 20

    def update_guessed_letters(self, letter):
        self.guessed_letters.append(letter)

    def update_word():
        pass

    def reset(self):
        self.guessed_letters = []
        self.words = []
        self.errors = 0

    def set_word_difficulty(self,lvl):
        if lvl == "easy":
            self.word_max_length = 6
        if lvl == "medium":
            self.word_min_length = 6
            self.word_max_length = 14
        if lvl == "hard":
            self.word_min_length = 14
            self.word_max_length = 22
    
    def pick_random_word(self):
        return random.choice(self.words)
    
    @staticmethod
    def draw_word(screen, word, guessed, text_color, font):
        display_word = ""
        for letter in word:
            if letter in guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        text = font.render(display_word, 1, text_color)
        screen.blit(text,(100,400))
    
    def load_words_from_file(filename):
        phrases = []
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip() 
                phrases.append(line)
        return phrases

    def validate_word(self, word):
        return word.isalpha() and len(word) <= self.word_max_length
    
    # def split_to_words(phrase):





import pygame
import sys
from button import Button as Bt
from hangman_letters import *
from hangman_word import *
from hangman import *
from file_manager import load, is_file_valid, extract_category
from tkinter import *
from tkinter import filedialog, messagebox

WHITE = (255,255,255)
BLACK = (0,0,0)

class Game:
    def __init__(self,screen):
        self.screen = screen
        self.font_manager = FontManager()
        self.letter_manager = LetterManager(screen)
        self.word_manager = WordManager(screen)
        self.hangman_manager = HangmanManager()
        self.clock = pygame.time.Clock()
        self.category = ""

    def start(self):
        pygame.display.set_caption("Hangman")

        START_BG = pygame.image.load("images/start_background.png")

        self.screen.blit(START_BG, (0,0))

        START_TEXT = self.font_manager.get_font(80).render("HANGMAN", True, "#b68f40")

        START_RECT = START_TEXT.get_rect(center=(400,self.screen.get_size()[1] // 2))

        self.screen.blit(START_TEXT, START_RECT)

        start_panel_time = 500
        start_panel_active = True 
        next_panel_active = False

        while True:
         
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()

            if start_panel_active:
                if pygame.time.get_ticks() >= start_panel_time:
                    start_panel_active = False
                    next_panel_active = True

            elif next_panel_active:
                self.load_file()
        
            pygame.display.update()
            

    def load_file(self):
            
            # create and hide root window
            root = Tk()
            root.withdraw()
            
            # open filedialog to pick a file
            filepath = filedialog.askopenfilename(title="Select a file", filetypes=(("txt files", ".txt"),("all files", ".")), parent=None)

            # cutting ".txt"

            self.category = extract_category(filepath)

            if filepath:
                while not is_file_valid(filepath):
                    messagebox.showerror("FILE ERROR", "Check if the file is not empty and if it consists only of letters and spaces.")
                    self.load_file()
                words = load(filepath)
                self.word_manager.words = words
                self.main_menu()
            else:
                self.exit()   


    def choose_level(self):
        pygame.display.set_caption("Hangman Level Selection")

        while True:
            self.screen.fill(WHITE)

            LEVEL_BG = pygame.image.load("images/level_background.png")

            self.screen.blit(LEVEL_BG, (100,-50))

            LEVEL_MOUSE_POS = pygame.mouse.get_pos()

            LEVEL_TEXT = self.font_manager.get_font(40).render("CHOOSE GAME LEVEL", True, "#b68f40")

            LEVEL_RECT = LEVEL_TEXT.get_rect(center=(400,100))

            EASY_BUTTON = Bt(image=pygame.image.load("images/button_rect.png"),pos=[400,300],text_input="EASY", font=self.font_manager.get_font(40),base_color="#d7fcd4",hovering_color="White")

            MEDIUM_BUTTON = Bt(image=pygame.image.load("images/button_rect.png"),pos=[400,400],text_input="MEDIUM", font=self.font_manager.get_font(40),base_color="#d7fcd4",hovering_color="White")

            HARD_BUTTON = Bt(image=pygame.image.load("images/button_rect.png"),pos=[400,500],text_input="HARD", font=self.font_manager.get_font(40),base_color="#d7fcd4",hovering_color="White")

            self.screen.blit(LEVEL_TEXT,LEVEL_RECT)

        
            for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
                button.changeColor(LEVEL_MOUSE_POS)
                button.update(self.screen)

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if EASY_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                        self.word_manager.set_word_difficulty("easy")
                    if MEDIUM_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                        self.word_manager.set_word_difficulty("medium")
                    if HARD_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                        self.word_manager.set_word_difficulty("hard")
                    self.play()
                

            pygame.display.update()


    def main_menu(self,play_sound=True):
        pygame.display.set_caption("Hangman Menu")

        menu_sound = pygame.mixer.Sound('sounds/menu_music.mp3')

        if play_sound:
            menu_sound.play()

        while True:
            self.screen.fill(WHITE)

            MENU_BG = pygame.image.load("images/menu_background.jpg")

            self.screen.blit(MENU_BG, (0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.font_manager.get_font(60).render("MAIN MENU", True, "#b68f40")

            MENU_RECT = MENU_TEXT.get_rect(center=(400,100))

            PLAY_BUTTON = Bt(image=pygame.image.load("images/button_rect.png"),pos=[400,300],text_input="PLAY", font=self.font_manager.get_font(40),base_color="#d7fcd4",hovering_color="White")

            QUIT_BUTTON = Bt(image=pygame.image.load("images/button_rect.png"),pos=[400,425],text_input="QUIT", font=self.font_manager.get_font(40),base_color="#d7fcd4",hovering_color="White")

            self.screen.blit(MENU_TEXT,MENU_RECT)

        
            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_sound.stop()
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.choose_level()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.exit()
            pygame.display.update() 


    def play(self, play_sound=True):
        pygame.display.set_caption("Hangman Game")

        game_sound = pygame.mixer.Sound('sounds/easy_music.mp3')

        if play_sound:
            game_sound.play()

        self.hangman_manager.load_hangman_images("images/hangman")

        word = self.word_manager.pick_random_word().upper()

        letters = self.letter_manager.get_letters()

        game_font = self.font_manager.get_font(20)

        CATEGORY_TEXT = game_font.render(self.category, True, "#b68f40")

        CATEGORY_RECT = CATEGORY_TEXT.get_rect(center=(self.screen.get_size()[0] // 2, 50))

        def sleep_after_result():
            pygame.time.wait(4000)

       
        def refresh_game_screen():

            self.screen.fill(WHITE)
            self.screen.blit(CATEGORY_TEXT, CATEGORY_RECT)
            self.letter_manager.draw_letters(self.screen,letters,BLACK,game_font)
            self.word_manager.draw_word(self.screen,word,self.word_manager.guessed_letters,BLACK,game_font)
            self.hangman_manager.draw_hangman(self.screen)


        def check_game_over():
            if self.hangman_manager.is_hangman_alive() and self.word_manager.is_word_in_guessed_letters(word):
                user_won()
            if not self.hangman_manager.is_hangman_alive():
                user_lost()


        def user_won():
            game_sound.stop()
            win_sound = pygame.mixer.Sound('sounds/star.wav')
            win_sound.play()
            sleep_after_result()
            self.post_play("WON")
          
            

        def user_lost():
            game_sound.stop()
            game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')
            game_over_sound.play()
            sleep_after_result()
            self.post_play("LOST")
            

        
        def handle_mouse_click(mouse_pos):
            m_x, m_y = mouse_pos
            for letter in letters:
                l_x, l_y, ltr, visible = letter
                if visible:
                    if self.letter_manager.is_letter_clicked(l_x,l_y,m_x,m_y):
                        self.word_manager.update_guessed_letters(ltr)
                        letter[3] = False
                        if ltr not in word:
                            self.hangman_manager.hangman_status += 1


        FPS = 60
        while self.hangman_manager.is_hangman_alive():
            # while loop runs with FPS speed
            self.clock.tick(FPS)
            
            MOUSE_POS = pygame.mouse.get_pos()

            # loop through event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    handle_mouse_click(MOUSE_POS)
                    
            #update the display       
            refresh_game_screen()
            pygame.display.update()

            # check whether game is over
            check_game_over()
    
    
    def post_play(self, game_result):


        while True:
            self.screen.fill(WHITE)

            POST_PLAY_BG = pygame.image.load("images/menu_background.jpg")

            self.screen.blit(POST_PLAY_BG, (0,0))

            POST_PLAY_MOUSE_POS = pygame.mouse.get_pos()

            POST_PLAY_TEXT = self.font_manager.get_font(60).render("YOU " + str(game_result), True, "#b68f40")

            POST_PLAY_RECT = POST_PLAY_TEXT.get_rect(center=(400,100))

            RESET_BUTTON = Bt(image=pygame.image.load("images/button_rect.png"),pos=[400,300],text_input="RESET GAME", font=self.font_manager.get_font(40),base_color="#d7fcd4",hovering_color="White")

            NEXT_WORD_BUTTON = Bt(image=pygame.image.load("images/button_rect.png"),pos=[400,425],text_input="NEXT WORD", font=self.font_manager.get_font(40),base_color="#d7fcd4",hovering_color="White")

            self.screen.blit(POST_PLAY_TEXT,POST_PLAY_RECT)

        
            for button in [RESET_BUTTON, NEXT_WORD_BUTTON]:
                button.changeColor(POST_PLAY_MOUSE_POS)
                button.update(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RESET_BUTTON.checkForInput(POST_PLAY_MOUSE_POS):
                        self.reset_game()
                    if NEXT_WORD_BUTTON.checkForInput(POST_PLAY_MOUSE_POS):
                        self.reset()
                        self.play()
            pygame.display.update()                            


    def reset_game(self):
        run()


    def reset(self):
        words = self.word_manager.words
        word_min_length = self.word_manager.word_min_length
        word_max_length = self.word_manager.word_max_length
        self.font_manager = FontManager()
        self.letter_manager = LetterManager(self.screen)
        self.word_manager = WordManager(self.screen)
        self.word_manager.words = words
        self.word_manager.word_min_length = word_min_length
        self.word_manager.word_max_length = word_max_length
        self.hangman_manager = HangmanManager()
        self.clock = pygame.time.Clock()
        self.category = ""


    def exit(self):
        pygame.quit()
        sys.exit()


def set_up_game():

    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    return Game(SCREEN)

def run():
    game = set_up_game()
    game.start()

run()
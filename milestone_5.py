import random

word_list = ['banana', 'raspberry', 'satsuma', 'strawberry', 'pineapple']

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = ['' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        updated_guess = guess.lower()
        if updated_guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
            print(f'The word remains as: {self.word_guessed}')
            if self.num_letters == 0:
                print('Congratulations. You won the game!')
                return True
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word. Try again')
            print(f'You have {self.num_lives} lives left')
            print(f'The word remains as: {self.word_guessed}')
            if self.num_lives == 0:
                print('You lost! Unlucky.')
                return True

    def ask_for_input(self):
        while True:
            guess = input('Please enter a single letter:')
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.check_guess(input('Please enter a single letter:')):
            break



play_game(word_list)
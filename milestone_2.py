import random

word_list = ['banana', 'raspberry', 'satsuma', 'strawberry', 'pineapple']

word = random.choice(word_list)

guess = input('Please enter a single letter:')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')

else:
    print('Oops! THat is not a valid input.')


print(guess)
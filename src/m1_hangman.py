"""
Hangman.

Authors: Josh Krsek and Jacob Murray.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import random

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

# step 1


def main():
    min_length = int(input('What MINIMUM length do you want for the secret word?'))
    word = pick_word()
    while len(word) < min_length:
        word = pick_word()
    print(word)
    num_guess = allowed_guesses()
    list_blanks = init_blanks(word)
    #guesses_left = num_guess

    while True:
        print_blanks_with_letters(list_blanks)
        letter = guess()
        blanks2 = change_blanks(word, letter, list_blanks)
        num_guess = countdown(blanks2, num_guess, letter, word)
        if num_guess == 0:
            break
        if convert_str(blanks2) == word:
            break


    play_again = str(input('Play another game? (y/n)'))
    if play_again == 'y':
        main()
    else:
        print('Thanks for playing Hangman!')



def allowed_guesses():
    allowed_g = int(input('How many guesses do you want?'))
    return allowed_g

def pick_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
    words = string.split()

    r = random.randrange(0, len(words))
    item = words[r]
    return item

# step 2
def guess():
    letter = str(input('What letter do you want to try?'))
    return letter


# step 3
def init_blanks(item):
    blanks = []
    for i in range(len(item)):
        blanks = blanks + ['-']
    return blanks


def print_blanks_with_letters(blanks1):
    blank = ''
    for j in range(len(blanks1)):
        blank = blank + blanks1[j]
    print(blank)


def change_blanks(item1, guess1, blanks2):
    for k in range(len(blanks2)):
        if guess1 == item1[k]:
            blanks2[k] = guess1
    return blanks2


def convert_str(blanks1):
    blank = ''
    for j in range(len(blanks1)):
        blank = blank + blanks1[j]
    return blank



def countdown(blanks2,guesses_left,guess1,item1):
    for k in range(len(blanks2)):
        if blanks2[k] == guess1:
            print('Good guess! You still have', guesses_left, 'unsuccessful guesses left before you LOSE the game!')
            blanks3 = convert_str(blanks2)
            if blanks3 == item1:
                print('You win!')
            return guesses_left
    guesses_left = guesses_left - 1
    print('Sorry! There are no', guess1, 'letters in the secret word. You have', guesses_left, 'unsuccessful guesses left before you LOSE the game!')
    print()
    if guesses_left == 0:
        print('You lose! The secret word was:', item1)
    return guesses_left


# for i in length(item):
#     if guess == item[i]:

main()


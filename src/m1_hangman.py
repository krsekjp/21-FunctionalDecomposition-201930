"""
Hangman.

Authors: Josh Krsek and Jacob Murray.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import random

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

# step 1


def main():
    word = pick_word()
    print(word)
    num_guess = allowed_guesses()
    list_blanks = init_blanks(word)
    print_blanks_with_letters(list_blanks)

    letter = guess()
    check_ans(word, letter, list_blanks, num_guess)


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


def check_ans(item1, guess1, blanks2, guesses_left):
    blanks2copy = blanks2.copy()
    for k in range(len(blanks2)):
        if guess1 == item1[k]:
            blanks2[k] = guess1
    if blanks2 != blanks2copy:
        print('Good guess!')
    else:
        guesses_left = guesses_left - 1
        print('Sorry! There are no', guess1, 'letters in the secret word. You have', guesses_left, 'unsuccessful guesses left before you LOSE the game!')
    return guesses_left


# for i in length(item):
#     if guess == item[i]:

main()
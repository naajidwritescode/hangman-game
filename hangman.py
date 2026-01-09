# Hangman in python

import random

words = ("apple", "orange", "banana", "pineapple", "mango", "coconut")
hangman_art = {0: ("     ",
                   "     ",
                   "     "),

               1: ("  o  ",
                   "     ",
                   "     "),

               2: ("  o  ",
                   "  |  ",
                   "     "),

               3: ("  o  ",
                   " /|  ",
                   "     "),

               4: ("  o  ",
                   " /|\\ ",
                   "     "),

               5: ("  o  ",
                   " /|\\ ",
                   " /   "),

               6: ("  o  ",
                   " /|\\ ",
                   " / \\ ")}


def display_man(wrong_guess):
    print("*******************")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("*******************")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(random_word):
    print(" ".join(random_word))


def main():
    random_word = random.choice(words)
    hint = ["_"] * len(random_word)

    wrong_guess = 0
    guessed_letters = set()

    is_running = True

    while is_running:
        display_man(wrong_guess)
        display_hint(hint)
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue

        if guess in guessed_letters:
            print(f"{guess} has been guessed")
            continue

        guessed_letters.add(guess)

        if guess in random_word:
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    hint[i] = guess
        else:
            wrong_guess += 1
            print(f"\n{6 - wrong_guess} Turns Left!")

        if "_" not in hint:
            display_man(wrong_guess)
            display_answer(random_word)
            print("\nYOU WIN!")
            is_running = False
        if wrong_guess == 6:
            display_man(wrong_guess)
            print("\nYOU LOSE!")
            print(f"Answer was: {" ".join(random_word)}")
            is_running = False


main()

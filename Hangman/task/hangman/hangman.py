import random
import string

PLACEHOLDER = '-'
APP_NAME = "H A N G M A N"

msg_soon = "The game will be available soon."
msg_survived = "You survived!"
msg_hanged = "You are hanged!"
msg_guess = "Guess the word"
msg_input = "Input a letter: "
msg_thanks = """Thanks for playing!
We'll see how well you did in the next stage"""
msg_no_letter = "No such letter in the word"
msg_no_improvement = "No improvements"
msg_guessed = "You guessed the word!"
msg_already_typed = "You already typed this letter"
msg_only_single = "You should print a single letter"
msg_no_ascii_lower = "It is not an ASCII lowercase letter"
msg_menu = 'Type "play" to play the game, "exit" to quit: '

solutions = ['python', 'java', 'kotlin', 'javascript']
commands = ["exit", "play"]

typed = None
found = None
prev = None


def _get_any_solution():
    return random.choice(solutions)


def announce():
    print(APP_NAME)
    print(msg_soon)


def guess():
    print(APP_NAME)
    word = str(input(f"{msg_guess}: ").lower())
    if word not in solutions:
        print(msg_hanged)
    elif word in solutions:
        print(msg_survived)


def guess_random_word():
    print(APP_NAME)
    word = str(input(f"{msg_guess}: ").lower())
    r_word = _get_any_solution()
    if word != r_word:
        print(msg_hanged)
    elif word == r_word:
        print(msg_survived)


def guess_random_word_with_preview():
    print(APP_NAME)
    r_word = _get_any_solution()
    prev = f"{r_word[0:3]}{len(r_word[3:]) * PLACEHOLDER}"
    word = str(input(f"{msg_guess} {prev}: ").lower())
    if word != r_word:
        print(msg_hanged)
    elif word == r_word:
        print(msg_survived)


def _check_and_get_input():
    global prev, typed
    while True:
        print()
        print(prev)
        character = str(input(msg_input))
        if len(character) > 1:
            print(msg_only_single)
            continue
        if character not in string.ascii_lowercase:
            print(msg_no_ascii_lower)
            continue
        if character in typed:
            print(msg_already_typed)
            continue
        else:
            typed.append(character)
            return character


def guess_n_times(n: int = 8):
    global prev, found, typed
    r_word = _get_any_solution()
    prev = f"{len(r_word) * PLACEHOLDER}"
    found = []
    typed = []
    while n > 0:
        letter = _check_and_get_input()
        if letter in r_word:
            if letter in found:
                n -= 1
                print(msg_no_improvement)
            else:
                for i in range(0, len(r_word)):
                    if r_word[i] == letter:
                        prev_list = list(prev)
                        prev_list[i] = letter
                        prev = ''.join(prev_list)
                found.append(letter)
        else:
            print(msg_no_letter)
            n -= 1
        if n == 0:
            print(msg_hanged)

        if PLACEHOLDER not in prev:
            print()
            print(prev)
            print(msg_guessed)
            print(msg_survived)
            break

    print(msg_thanks)
    return None


def run():
    print(APP_NAME)
    _start_menu()
    guess_n_times()


def _start_menu():
    while True:
        command = input(msg_menu)
        if command not in commands:
            continue
        if command == commands[1]:
            break
        else:
            exit(0)


if __name__ == '__main__':
    run()

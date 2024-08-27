import random
import gspread
import string
from gallows import gallows  # Hangman art dictionary
import os
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('words')
words = SHEET.worksheet('unfiltered')

data = words.get_all_values()
words_list = sum(data, [])               # global variable
already_guessed = set()                  # global variable
width = os.get_terminal_size().columns   # See credit in README


def clear():
    """
    Function to clear unneeded text from the terminal during the game.
    This piece of code, and the idea that it could be used here,
    was obtained from Code Institute's Marko Tot. See readme file.
    """
    os.system("cls" if os.name == "nt" else "clear")


def display_intro():
    """
    Displays game title, empty gallows, and game rules.
    """
    title = 'HANGMAN\n'
    print('\n')
    print(title.center(width))
    rules = """
         ________
         | /                  The gallows await!
         |
         |         Guess all of the letters in a word before you're hung.
         |           Each wrong guess brings you closer to hanging from
        _|_            the gallows. All of the words are in the English
     __|_|_|______       language and contain only letters A through Z
                          in the English alphabet.
                                 Good luck!

    """
    print(rules.center(width))


def ask_for_player_name():

    """
    Asks player to input name. Calls function to validates that name
    is alpha only and greets player, else prompts for valid entry.
    """
    while True:
        name = input('Enter your name to start the game: \n').upper()
        if validate_user_name_as_alpha(name):
            clear()
            welcome_message = f'Hello, {name}! Welcome to Hangman! \n'
            print(welcome_message.center(width))
            break
    return name


def validate_user_name_as_alpha(nentry):
    """
    Checks whether user has input a name using only letters A-Z.
    If not, raises error, informs player of reasons, invites
    player to try again.
    """
    try:
        if not nentry.isalpha():
            raise TypeError(
                f'Name must consist of letters A-Z only.'
            )
    except TypeError as e:
        print(f'Invalid entry: {e} Please try again.')
        return False
    return True


def get_word():
    """
    Gets a random word from the list of words and make it uppercase,
    ensuring word has no spaces or hyphens and is 4 or more letters in length.
    """
    global words_list
    word = random.choice(words_list)
    while " " in word or "-" in word or len(word) < 4:
        word = random.choice(words_list)
    word = word.upper()
    return word


def display_underscores(word):
    """
    Gets the number of letters in the randomly chosen word, initially
    prints out an equal number of underscores. Tells player length of the word.
    Throughout play, prints correctly guessed letters and remaining underscores
    in the proper places.
    """
    global already_guessed
    word_length = len(word)
    if len(already_guessed) == 0:
        for letter in word:
            print('_', end=' ')
        print(f'\nThe word length is {word_length} letters. \n')
    else:
        for letter in word:
            if letter in already_guessed:
                print(letter, end=' ')
            else:
                """
                Below from a youtube video. Credit in readme.
                """
                print('_', end=' ')
    print('\n')


def ask_for_guess():
    """
    Asks player to guess a letter. Calls functions
    to validate input as a new single-letter guess.
    Continues until valid input received, returns guess.
    """
    global already_guessed
    while True:
        guess = input("Enter a letter: \n").upper()
        if not validate_ltrinput(guess):
            continue
        if check_if_already_guessed(guess):
            continue
        already_guessed.add(guess)
        return guess


def validate_ltrinput(typedin):
    """
    Checks whether user has input a single letter, else
    raises the relevant error and continues to ask
    for valid input until received.
    """
    alphabet = set(string.ascii_uppercase)
    try:
        if typedin not in alphabet:
            raise TypeError(
                f'Guess should be a single letter. You typed {typedin}.'
            )
    except (TypeError) as e:
        print(f'Invalid guess: {e} Please try again.')
        return False
    return True


def check_if_already_guessed(ltr):
    """
    Checks if user guess is already in set of guessed
    letters. If so, raises an error, informs user that
    they've already guessed the letter, and returns boolean
    value for the while loop in function where it is called.
    """
    global already_guessed
    try:
        if ltr in already_guessed:
            raise ValueError(f'You already guessed {ltr}.')
        else:
            return False
    except ValueError as e:
        print(f'{e} Try a different guess.')
        return True


def validate_yesorno(answer):
    """
    Checks whether user input is 'Y' for 'yes' or 'N' for 'no'
    (changed to upper at input), else raises an error and
    continues to ask for valid input until received.
    """
    alphabet = set(string.ascii_uppercase)
    try:
        if answer not in alphabet or answer not in ('N', 'Y'):
            raise TypeError(
                f'You typed {answer}. Please type Y or N.'
            )
    except (TypeError) as e:
        print(f'Invalid answer: {e}')
        return False
    return True


def start_game():
    word = get_word()
    lives = 6
    word_letters = set(word)
    global already_guessed
    print(gallows[6])
    while lives > 0 and len(word_letters) > 0:
        display_underscores(word)
        guess = ask_for_guess()
        if guess in word_letters:
            print(f'Good guess! {guess} is in the word. \n')
            word_letters.remove(guess)
            if len(word_letters) > 0:
                guesses_list = list(already_guessed)
                guesses_list.sort()
                guesses = ' '.join(guesses_list)
                print(f'These are your guesses so far: {guesses} \n')
        else:
            lives -= 1
            print(f"Too bad. {guess} isn't in the word. \n")
            print(gallows[lives])
            if lives > 0:
                print(f"You have {lives} wrong guess(es) "
                      "left before you're hung.\n"
                      )
                guesses_list = list(already_guessed)
                guesses_list.sort()
                guesses = ' '.join(guesses_list)
                print(f'These are your guesses so far: {guesses} \n')
    if lives > 0 and len(word_letters) == 0:
        for letter in word:
            print(letter, end=' ')
        print('\nCongratulations! You won!\n')
        print(gallows[-1])
    if lives == 0 and len(word_letters) > 0:
        print(f"Game over. The word was {word}. Better luck next time!")
    if lives == 0 or len(word_letters) == 0:
        print('Do you want to play again?')
    """
    Resets set of guesses to empty set for the next round of play.
    """
    already_guessed = set()
    """
    Allows player to choose whether to play again or exit.
    """
    while True:
        newgame = input('Enter Y for yes or N for no: \n').upper()
        if not validate_yesorno(newgame):
            continue
        if validate_yesorno(newgame):
            if newgame == 'Y':
                print("Great! let's play again!")
                clear()
                start_game()
                return False
            elif newgame == 'N':
                clear()
                print('Thanks for playing!')
                print(gallows[-2])
                return False
                exit()
        return False


def main():

    clear()
    display_intro()
    ask_for_player_name()
    start_game()


main()

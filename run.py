import random
import gspread
import string
from gallows import gallows
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
words_list = sum(data, [])          # words_list is global var
already_guessed = set()             # global variable
width = os.get_terminal_size().columns


def clear():                      # see credits in readme file
    """
    Function to clear unneeded text from the terminal throughout the game.
    """
    os.system("cls" if os.name == "nt" else "clear")


def display_intro():

    title = 'HANGMAN\n'
    print(title.center(width))
    rules = "Guess all of the letters in a word before you're hung.\n"
    print(rules.center(width))


def ask_for_player_name():

    """
    Asks player to input name. Calls function to validates that name
    is alpha only and greets player, else prompts for valid entry.
    """
    while True:
        name = input('Please enter your name: \n')
        if validate_user_name_as_alpha(name):
            clear()
            welcome_message = f'Hello, {name}! Welcome to Hangman! \n'
            print(welcome_message.center(width))
            print(gallows[6])
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
    print(f'The word is: {word}. (Do not forget to remove this!\n')
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
        print(f'The word length is {word_length} letters. \n')
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
    Checks whether user has input 'Y' or 'y' for 'yes'
    or 'N' or 'n' for 'no', else raises an error and
    continues to ask for valid input until received.
    """
    alphabet = set(string.ascii_uppercase)
    try:
        if answer not in alphabet or answer not in ('N', 'Y'):
            raise TypeError(
                f'Please type Y for yes or N for no. You typed {answer}.'
            )
    except (TypeError) as e:
        print(f'Invalid answer: {e} Please try again.')
        return False
    return True
        

def start_game():
    word = get_word()
    lives = 6
    word_letters = set(word)
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

    while True:
        newgame = input('Enter Y for yes or N for no: \n').upper()

        if not validate_yesorno(newgame):
            print(f'this was typed in: {newgame} We have come this far!')
            continue
        print(f'{newgame} is being returned from the while loop')

        if validate_yesorno(newgame):
            if newgame == 'Y':
                print("Great! let's play again!")
                start_game()
                return False
            elif newgame == 'N':
                print('Thanks for playing!')
                return False
                exit()

        
    



def main():

    display_intro()
    ask_for_player_name()
    start_game()
    


main()

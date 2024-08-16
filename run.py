import random
import gspread
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
def flatten_sum(data):
    return sum(data, [])

single_list = flatten_sum(data)

def display_game_title():
    print("HANGMAN")

def display_game_rules():
    print("here are the rules")

def ask_for_player_name():
    name = input("Enter you name: \n")
    print(f"Hello, {name}! Welcome to Hangman \n")
    return name

def get_word():
    """
    Get a random word from the list of words
    """
    word = random.choice(single_list)
    print(f'Word "{word}" successfully generated by program')
    return word

def display_underscores(word):
    """
    Gets the number of letters in the randomly chosen word
    and prints out an equal number of underscores to let player know
    how many letters are in the word.
    """
    for letter in word:
        print("_", end= " ")
    print("\n")

def ask_for_guess():
    """
    Asks player to guess a letter, 
    changes input to uppercase, calls function
    to validate input as a letter, and continues to ask
    for a letter input until a letter is input.
    """
    while True:
        guess = input("Enter a letter: \n")
        if validate_guess(guess):
            print(f'You guessed {guess}')
            break
    return guess


def validate_guess(typed):
    """
    Checks whether user has input a letter. If not,
    raises an error telling the user their input
    is invalid and asking for a letter input.
    """
    try:
        if not typed.isalpha():
            raise TypeError(
                f'Guess should be a letter. You typed {typed}.'
            )
    except TypeError as e:
        print(f'Invalid guess: {e} Please try again.')
        return False
    return True

def main():
    """
    Runs main program
    """
    display_game_title()
    display_game_rules()
    ask_for_player_name()
    word = get_word()
    display_underscores(word)
    ask_for_guess()
    
main()
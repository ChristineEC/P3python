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
display_game_title()

def display_game_rules:
    ...

def ask_for_player_name():
    name = input("Enter you name: \n")
    print(name)
    return name

def greet_player_by_name(name):
    print(f"Hello, {name}! Welcome to Hangman /n")

def ask_for_guess():
    guess = input("Enter a letter: \n")
    ...


def get_word():
    """
    Get a random word from the list of words
    """
    word = random.choice(single_list)
    print(word)
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



  

def main():
    """
    Runs main program
    """

    ask_for_player_name()
    greet_player(name)
    word = get_word()
    display_underscores(word)

main()
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
words_list = sum(data, [])          #words_list is global var
already_guessed = set()             #global variable
width = os.get_terminal_size().columns   #credit Marko portfolio 3 project in GitHub for this piece of code


def display_intro():
    title = 'HANGMAN'
    print(title.center(width))    #credit W3Schools for centering text in terminal
    rules = """Guess all of the letters in a word before you're hung. 
            For each wrong guess, a new body part will display under the gallows.\n"""
    print(rules.center(width))

def ask_for_player_name():
    """
    Asks player to input name. Calls function to validates that name 
    is alpha only and greets player, else prompts for valid entry.
    """
    while True:
        name = input('Please enter your name: \n')
        if validate_user_name_as_alpha(name):
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
    print(f'The word is: {word} \n')
    return word

#def display_hangman()

def display_underscores(word):
    """
    Gets the number of letters in the randomly chosen word, prints out 
    an equal number of underscores. Tells player the length of the word.
    """
    global already_guessed
    word_length = len(word)
    print(f'\nThe word length is {word_length} letters.')
    for letter in word:
        if letter in already_guessed:
            print(letter, end = ' ')
        else: print("_", end= " ") #got this method from a youtube video. need to credit if not removed later
    print("\n")

def ask_for_guess():
    """
    Asks player to guess a letter. Calls functions to validate input as a new single letter
    and continues to ask for a new letter input. Returns a valid guess.
    """
    global already_guessed  
    while True:
        guess = input("Enter a letter: \n").upper()
        if not validate_guess(guess):
            continue
        if check_if_already_guessed(guess):
            continue
        already_guessed.add(guess)
        return guess

def validate_guess(typedin):
    """
    Checks whether user has input a single letter. If not, raises the relevant error 
    and continues to ask for valid input until received.
    """
    alphabet = set(string.ascii_uppercase)
    try:
        if not typedin in alphabet:
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
                print(f'These are your guesses so far: {already_guessed} \n')
            
        else:
            lives -= 1
            print(f"Too bad. {guess} isn't in the word. \n")
            if lives > 0:
                print(f"You have {lives} wrong guess(es) left before you're hung.")
                print(f'These are your guesses so far: {already_guessed}')
    
    if lives > 0 and len(word_letters) == 0:
        print("Congratulations! You won!")

    if lives == 0 and len(word_letters) > 0:
        print(f"Oh, no! You've been hung! The word was {word}. Better luck next time.")
        """
        Need function to change hangman graphic. Move function to add to set of guesses into
        this function"
        """

def main(): 
    display_intro()
    print(gallows[6])
    ask_for_player_name()
    start_game()


main()
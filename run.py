import random
import gspread
import string
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
def flatten_sum(data):                               #make sure to credit this line
    """
    Changes the list of lists (each containing
    a single word) obtained from google sheet
    into a single list of words
    """
    return sum(data, [])

single_list = flatten_sum(data)                   #Global variable
already_guessed = set()                           #Global variable

def display_game_title():
    print("HANGMAN")

def display_game_rules():
    print("Here are the rules \n")

def ask_for_player_name():
    """
    Asks player to input name. Validates
    that it is alpha only, else prompts
    for alpha-only name.
    """
    while True:
        name = input("Please enter your name: \n")
        if validate_user_name_as_alpha(name):
            print(f"Hello, {name}! Welcome to Hangman! \n")
            break
    return name

def validate_user_name_as_alpha(nentry):
    """
    Checks whether user has input a name using only
    letters A-Z. Raises error if not.
    """
    print('Validating user name as alpha')
    try:
        if not nentry.isalpha():
            raise TypeError(
                f"Name must consist of letters A-Z only."
            )
    except TypeError as e:
        print(f'Invalid entry: {e} Please try again.')
        return False
    return True

def get_word():
    """
    Get a random word from the list of words
    and make it uppercase
    """
    word = random.choice(single_list)
    print(f'Word "{word}" successfully generated by program')
    word = word.upper()
    print(f'word now changed to uppercase: {word}')

    return word

def display_underscores(string):
    """
    Gets the number of letters in the randomly chosen word
    and prints out an equal number of underscores. Tells
    player the length of the word.
    """
    word_length = len(string)
    print(f'The word length is {word_length} letters.')
    for letter in string:
        print("_", end= " ") #got this method from a youtube video. need to credit if not removed later
    print("\n")

def ask_for_guess():
    """
    Asks player to guess a letter. Call function 
    to validate input as a single letter
    else raises relevant error and asks player
    again for letter input. Calls function to validate
    that guess has not been repeated, and continues to 
    ask for a (new) letter input until a valid letter
    is received. Appends the valid guess to  set of 
    guessed letters and returns that set.
    """
    #global already_guessed

    while True:
        guess = input("Enter a letter: \n").upper()
        if validate_guess(guess):
            print('Guess is of valid form.')
            if check_already_guessed(guess):
                print(f'{guess} has not been guessed')
                print(f'You guessed {guess}')
                break
    return guess

def validate_guess(typedin):
    """
    Checks whether user has input a single letter. 
    If not, raises the relevant error and continues
    to ask for valid input until received.
    """
    print('Validating that the guess is a single letter')
    alphabet = set(string.ascii_uppercase)
    try:
        if not typedin in alphabet:
            print ('Entry not in alphabet.')
            raise TypeError(
                f'Guess should be a single letter. You typed {typedin}.'
            )
    except (TypeError) as e:
        print(f'Invalid guess: {e} Please try again.') 
        return False
    return True

def check_already_guessed(ltr):
    global already_guessed
    print("Checking to see if already guessed")
    try:
        if ltr in already_guessed:
            raise ValueError('You already guessed {ltr}.')
    except ValueError as e:
        print(f'{e} Try a different guess.')
        return False
    return True

def add_to_set_of_guesses(newguess):
    """ 
    Appends the valid guess to set of 
    guessed letters and returns the increased set.
    """
    already_guessed.add(newguess)
    """
    sort the set of guesses for display in terminal
    """
    print(f'New set of guesses {already_guessed}')

    return already_guessed
    print(f'sorted({already_guessed})')


"""
def compare_guess(ltr):
    #global already_guessed

    print('Checking to see if the guess is in the word.')

    if ltr in word_letters:
        word_letters.remove(ltr)
        print(f'Good guess! {ltr} is in the word.')
        """ 
        """
        Need funtion to display correct guesses
        """
        """

    else:
        print(f"{ltr} isn't in the word.")
        already_guessed.add(ltr)
        print(f'list.sorted({already_guessed})')
        """
        """
        Need function to change hangman graphic
        and decrease player's remaining chances.
        Inform player of remaining chances.
        Move function to add to set of guesses into
        this function"

        """


def main():
    word = get_word()
    word_letters = set(word) 
    display_game_title()
    display_game_rules()
    ask_for_player_name()
    print(word_letters)
    #display_gallows()
    display_underscores(word)
    already_guessed = set()

    """
    Runs main loop
    """
    
    guess = ask_for_guess()
    already_guessed = add_to_set_of_guesses(guess)
    print(f"These are the letters you've guessed so far: {already_guessed}")
    compare_guess(guess)
    print(f' Word letters have been decreased to {word_letters} \n')
    guess = ask_for_guess()
    already_guessed = add_to_set_of_guesses(guess)
    print(f"These are the letters you've guessed so far: {already_guessed}")
    compare_guess(guess)
    print(f' Word letters have been decreased to {word_letters} \n')
    guess = ask_for_guess()
    already_guessed = add_to_set_of_guesses(guess)
    print(f"These are the letters you've guessed so far: {already_guessed}")
    compare_guess(guess)
    print(f' Word letters have been decreased to {word_letters} \n')


main()
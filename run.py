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
single_list = flatten_sum(data)     #Global variable
already_guessed = set()             #global variable

def flatten_sum(data):    #make sure to credit this line
    """
    Changes the list of lists (each containing
    a single word) obtained from google sheet
    into a single list of words.
    """
    return sum(data, [])

def display_intro():
    print('HANGMAN')
    print('-------')
    print("""RULES\nPlayer's objective is to guess 
        all letters in a word of a given length. 
        For each wrong letter guessed, a new body 
        part appears under the gallows. Player must 
        guess all letters before the whole body
        is hung.""")

def ask_for_player_name():
    """
    Asks player to input name. Validates
    that it is alpha only and greets player, 
    else prompts for alpha-only name.
    """
    while True:
        name = input('Please enter your name: \n')
        if validate_user_name_as_alpha(name):
            print(f'Hello, {name}! Welcome to Hangman! \n')
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
                f'Name must consist of letters A-Z only.'
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
    global single_list
    word = random.choice(single_list)
    print(f'Word "{word}" successfully generated by program')
    word = word.upper()
    print(f'word now changed to uppercase: {word}')

    return word

#def display_hangman()

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
    and continues to ask for letter input.
    Returns valid form.
    """
    global already_guessed  
    while True:
        guess = input("Enter a letter: \n").upper()
        if not validate_guess(guess):
            print('Guess is of invalid form.')
            if not validate_guess(guess) or not check_if_already_guessed(guess):
                print(f'{guess} has already been guessed. Try again')
                return False
        return True
    
    return guess

print(f'{guess} from the while loop')

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

def check_if_already_guessed(ltr):
    global already_guessed
    print("Checking to see if already guessed")
    try:
        if ltr in already_guessed:
            raise ValueError(f'You already guessed {ltr}.')
    except ValueError as e:
        print(f'{e} Try a different guess.')
        return False
    return True

def play_valid_guess(goodletter):
    word = get_word()
    print(word)
    lives = 6
    word_letters = set(word)
    print("Ready to use the valid letter to play")
    
    while lives > 0 and len(word_letters) > 0:

        if goodletter in word_letters:
            print(f'Good guess! {goodletter} is in the word.')
            word_letters.remove(goodletter)
            print(f'These are your guesses so far: {already_guessed} \n')
            print(f'FOR ME: letters remaining in {word_letters} in play \n')
            #print(letter for letter in word else '_' for letter)
        else:
            lives -= 1
            print(f"Too bad. {ltr} isn't in the word.")
            print(f'These are your guesses so far: {already_guessed} \n')
            #print(letter for letter in word else '_' for letter)
        

        """
        Need function to change hangman graphic
        and decrease player's remaining chances.
        Inform player of remaining chances.
        Move function to add to set of guesses into
        this function"
        """
def prelims():


    """
    Runs main loop
    """
def main(): 
    display_intro()
    ask_for_player_name()
    #display_gallows()
    display_underscores(word) 
    guess = ask_for_guess()
    print(f"FROM MAIN - These are the letters you've guessed so far: {already_guessed}")
    play_valid_guess(guess)
    print(f' Word letters have been decreased to {word_letters} \n')
    #already_guessed = add_to_set_of_guesses(guess)
    print(f"These are the letters you've guessed so far: {already_guessed}")
    compare_guess(guess)
    
    guess = ask_for_guess()
    already_guessed = add_to_set_of_guesses(guess)
    print(f"These are the letters you've guessed so far: {already_guessed}")
    compare_guess(guess)
    print(f' Word letters have been decreased to {word_letters} \n')

prelims()
main()
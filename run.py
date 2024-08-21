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
words_list = sum(data, [])          #words_list is global var
already_guessed = set()             #global variable


def display_intro():
    print('HANGMAN')
    print('-------')
    print("""RULES\nGuess all of the letters in a word before you're hung. \n""")

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
    global words_list
    word = random.choice(words_list)
    while " " in word or "-" in word or len(word) < 4:
        word = random.choice(words_list)
    word = word.upper()
    print(f'Valid word generated and changed to uppercase: {word} \n')
    return word

#def display_hangman()

def display_underscores(word):
    """
    Gets the number of letters in the randomly chosen word
    and prints out an equal number of underscores. Tells
    player the length of the word.
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
    Asks player to guess a letter. Calls function 
    to validate input as a single letter
    and continues to ask for letter input.
    Returns valid form.
    """
    global already_guessed  
    while True:
        guess = input("Enter a letter: \n").upper()
        if not validate_guess(guess):
            print('Guess not validated. Printing from inside the ask-for-guess function.')
            continue
        if check_if_already_guessed(guess):
            print(f'{guess} has already been guessed. Try again This is from inside the ask-for-guess function')
            continue
        already_guessed.add(guess)
        print(f'The {guess}, {guess} is about to be returned from the ask loop')
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

def check_if_already_guessed(ltr):
    global already_guessed
    print("Checking to see if already guessed")
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
            print(f'These are your guesses so far: {already_guessed} \n')
            print(f'FOR ME: {len(word_letters)} word_letters remaining \n')
            
        else:
            lives -= 1
            print(f"Too bad. {guess} isn't in the word. \n")
            print(f'These are your guesses so far: {already_guessed} \n')
            #print(letter for letter in word else '_' for letter)
    
    if lives > 0 and len(word_letters) == 0:
        print("Congratulations! You won!")
        
    if lives == 0 and len(word_letters) > 0:
        print("Oh, no! You've been hung! Better luck next time.")
        """
        Need function to change hangman graphic
        and decrease player's remaining chances.
        Inform player of remaining chances.
        Move function to add to set of guesses into
        this function"
        """

def main(): 
    display_intro()
    ask_for_player_name()
    start_game()


main()
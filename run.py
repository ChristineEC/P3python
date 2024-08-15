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

single_list.append("zebrazebra")
print(single_list[-1])

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
    word = get_word()
    display_underscores(word)

main()
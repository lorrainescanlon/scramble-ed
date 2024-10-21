import gspread
from google.oauth2.service_account import Credentials
from os import system, name

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('edsongs')

songs = SHEET.worksheet('songs')
data = songs.get_all_values()
scores = SHEET.worksheet('scores')
score_data = scores.get_all_values()

"""
class User(object):
    name = ""
    score = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score

"""


def get_username():
    """
    Get username input from user
    """

    while True:
        print("Welcome to Scramble Ed\n")
        print("Can you guess the Ed Sheeran song title before Ed tunes his guitar?\n")
        print("You have 3 attempts to unscramble the song title\n")
        print("Enter a username to start the game, max length 12 characters\n")

        username = input("Username here:\n")

        if validate_username(username):
            print("Username is valid")
            break
    return username



def validate_username(name):
    """
    Checks that the username entered does not exceed 12 characters
    """
    try:
        if len(name) > 12:
            raise ValueError(
                "Username exceeds length"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True

def select_level(username):
    """
    Prompts the user to enter a level of difficulty.
    1. Consists of 1 word song titles.
    2. Consists of 2 word song titles.
    3. Consists of 3 word song titles.
    """
    while True:
        print(f"Lets get started {username}\n")
        print("Please choose a level of difficulty: 1, 2, or 3\n")
        print("1 - 1 Word Song Titles\n")
        print("2 - 2 Word Song Titles\n")
        print("3 - 3 Word Song Titles\n")

        level_choice = ""
        level_choice = input("Enter 1, 2 or 3: \n")

        if validate_choice(level_choice):
            print("Choice is valid")
            break
    return level_choice

def validate_choice(choice):
    """
    Checks that the level entered is 1, 2 or 3
    """
    try:
        if choice not in ("1", "2", "3"):
            raise ValueError(
                "Incorrect level entered"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def clear():
    """
    Clears console screen
    """

    #to clear windows machines
    if name == 'nt':
        _ = system('cls')
    
    #to clear mac and linux machines
    else:
        _ = system('clear')
    

username = get_username()
select_level(username)

#print(score_data)



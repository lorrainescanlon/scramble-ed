import gspread
import random
import array
from google.oauth2.service_account import Credentials
from os import system, name
from random import shuffle
from art import game_title

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('edsongs')

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
    game_title()

    while True:
        #print("Welcome to Scramble Ed\n")
        #print("Can you guess the Ed Sheeran song title before Ed tunes his guitar?\n")
        #print("You have 3 attempts to unscramble the song title\n")
        #print("Enter a username to start the game, max length 12 characters\n")

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
    #clear()
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

def load_words(choice):
    """
    Load songs list into a list according to level choice
    """

    titles_to_use = []
    songs = SHEET.worksheet('songs')
    
    if choice == "1":
        titles_to_use = songs.col_values(1)
    elif choice == "2":
        titles_to_use = songs.col_values(2)
    elif choice == "3":
        titles_to_use = songs.col_values(3)
    return titles_to_use


def random_title(titles_to_use):
    """
    Pick a random title from the list 'title_to_use"
    """

    return random.choice(titles_to_use)

def split_and_scramble(title):
    """
    Split song titles, scramble words and put back together as a string
    """
    # split the song title into list items
    title_arr = title.split(" ")
    # create a new list
    title_arr_scrambled = []
    for word in title_arr:
        # split each word into a list
        word = list(word)
        # shiffle the list items or letters
        shuffle(word)
        # create a new shuffled word by joining the letters together
        new_word = ''.join(word)
        # add new shuffled word to list
        title_arr_scrambled.append(new_word)

    print(f"print title_arr_scrambled {title_arr_scrambled}")
    #return string created by joining shuffled list words together
    return " ".join(title_arr_scrambled)


def scramble_title(title):
    """     
    Shuffle the random title to return a scrambled word to the user
    """
    (title) = list(title)
    shuffle(title)
    return ''.join(title)
 

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
level_choice = select_level(username)
#print(level_choice)

titles_to_use = load_words(level_choice)
#print(titles_to_use)

chosen_title = random_title(titles_to_use)
print(chosen_title)

scrambled_title = scramble_title(chosen_title)
#print(scrambled_title)

new_title = split_and_scramble(chosen_title)
print(new_title)









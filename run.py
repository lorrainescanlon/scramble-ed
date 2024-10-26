import gspread
import random
import array
import time
import sys
from google.oauth2.service_account import Credentials
from os import system, name
from random import shuffle
from art import game_title, guitar

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
    clear()
    while True:
        print(f"\n\n{username} please choose a level of difficulty: 1, 2, or 3\n")
        print("1 - 1 Word Song Titles\n")
        print("2 - 2 Word Song Titles\n")
        print("3 - 3 + Word Song Titles\n")
        print("quit to exit")

        level_choice = ""
        level_choice = input("Enter 1, 2 or 3: \n")

        if level_choice == "quit":
            clear()
            get_username()
        elif validate_choice(level_choice):
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
    Load songs from worksheet column into a list according to level choice
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
    Split song title into list items
    scramble words and add to new list
    assemble scrambled words as a string
    return scrambled string
    """
    title_arr = title.split(" ")
    title_arr_scrambled = []
    for word in title_arr:
        word = list(word)
        shuffle(word)
        new_word = ''.join(word)
        title_arr_scrambled.append(new_word)
        scrambled_title = " ".join(title_arr_scrambled)
    if scrambled_title != title:
        return scrambled_title
    else:
        split_and_scramble(title)


def load_question(username, scrambled_title, chosen_title):
    """
    loads the scrambled title and prompts the player to 
    guess. Calls valiadtion function and checks answer. 
    before the countdown timer expires
    """
    clear()
    print(f"\n\nGood Luck {username}, your Scrambled Ed song title is:\n")
    typewriter_print(scrambled_title)
    #print(f"{scrambled_title}\n")

    now = time.time()
    end_time = now + 20

    while True:
        guess = input(f"Your Guess here:\n")
        if guess == "quit":
            print(f"The correct answer was {chosen_title}\n")
            break
        elif validate_guess(guess, chosen_title):
            if guess == chosen_title:
                print(f"\nWell Done You've guessed it\n")
                break
            else:
                clear()
                print(f"\nWrong guess, please try again\n")
                print(f"Your chosen song title is: {scrambled_title}") 
            
    play_again(username)    



def validate_guess(guess, chosen_title):
    """
    Checks that the users guess contains the correct characters
    """

    guess_compare = list(guess)
    title_compare = list(chosen_title)

    try:
        if len(guess_compare) < len(title_compare):
            raise ValueError(
                "You have used too few characters"
            )
        elif len(guess_compare) > len(title_compare):
            raise ValueError(
                "You have used too many characters"
            )    
        elif sorted(guess_compare) != sorted(title_compare):
            raise ValueError(
                "Incorrect characters used"
            )

    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False
    return True

def typewriter_print(title_string):
    for char in title_string:
        time.sleep(.3)
        sys.stdout.write(char)
        sys.stdout.flush()
        
    print(f"\n")


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
    
def play_again(username):
    """
    Returns the user to the level choice section if yes
    or the Intro page if no
    """
    print("Would you like to play again?")
    play = input(f"y for yes or n for no :\n")

    if play =="y":
        play_game(username)
    else:
        print(f"\nSorry you're leaving {username}\n")
        bye()
        #main()

def bye():
    print(f"Goodbye Now\n")



def play_game(username):
  
    level_choice = select_level(username)
    titles_to_use = load_words(level_choice)
    chosen_title = random_title(titles_to_use)
    scrambled_title = split_and_scramble(chosen_title)
    load_question(username, scrambled_title, chosen_title)


def main():
    username = get_username()
    play_game(username)


main()



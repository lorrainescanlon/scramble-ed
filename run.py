import gspread
import random
import array
import time
import sys
from google.oauth2.service_account import Credentials
from os import system, name
from random import shuffle
from art import game_title_banner, guitar, score_board_banner, game_over_banner
from colours import tcolours

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('edsongs')
SCORE = 0
LIVES = 3

def get_username():
    """
    Display Game title banner
    Get username input from user
    """
    print(f"{tcolours.green}{game_title_banner[0]}{tcolours.end}")
    print(f"{game_title_banner[1]}")

    while True:
        username = input("Username here:\n")

        if validate_username(username):
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
        print(f"\n{tcolours.red}Invalid data: {e}, please try again.{tcolours.end}\n")
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
        print(f"\n{username} please choose a level of difficulty: 1, 2, or 3\n")
        print("1 - 1 Word Song Titles\n")
        print("2 - 2 Word Song Titles\n")
        print("3 - 3 + Word Song Titles\n")

        level_choice = ""
        level_choice = input("Enter 1, 2 or 3: \n")

        if validate_choice(level_choice):
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
        clear()
        print(f"\n{tcolours.red}Invalid data: {e}, please try again.{tcolours.end}")
        return False
    return True


def load_words(choice):
    """
    Load songs from worksheet column into a list according to level choice
    """
    titles_to_use = []
    songs = SHEET.worksheet('songs')
    titles_to_use = songs.col_values(int(choice))
    print(f"{titles_to_use}")
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


def load_question(username, scrambled_title, chosen_title, level_choice, guitar):
    """
    loads the scrambled title and prompts the player to enter a guess.
    Calls the timer function to set a timer for the game. 
    Checks answer, if correct increases score and prompts user to play again.
    If incorrect prompts the user to try again until lives are 0 are time is up.
    """
    clear()
    print(f"\n\nGood Luck {username}, your Scrambled Ed song title is:\n")
    typewriter_print(scrambled_title)
    print(f"{tcolours.blue}{(guitar[3])}{tcolours.end}")
    time_up = set_time()

    global LIVES


    while check_lives(username, chosen_title) and check_time(username, time_up, chosen_title):
        guess = input(f"Your Guess here:\n")
        if guess == "quit":
            reason = "You Quit"
            end_game(username, reason, chosen_title)
            #print(f"The correct answer was {tcolours.green}{chosen_title}{tcolours.end}\n")
            break
        elif guess == chosen_title:
            print(f"\n{tcolours.green}Well Done You've guessed it{tcolours.end}\n")
            increase_score(level_choice)
            play_again(username)
            break
        else: 
            clear()
            print(f"\n{tcolours.red}Wrong guess, please try again{tcolours.end}\n")
            loose_a_life()
            print(f"Your chosen song title is: {scrambled_title}\n")        


def set_time():
    """
    Set time for game to 20 seconds
    """
    NOW = time.time()
    timer = NOW + 30
    return timer


def check_lives(username, chosen_title):
    """
    Check if user has lives left
    """
    global LIVES
    reason = "You have run out of Lives"
    if LIVES == 0:
        end_game(username, reason, chosen_title)
    else:
        return True


def check_time(username, time_up, chosen_title):
    """
    Check if the time is up
    """
    time_left = time_up - (time.time())
    reason = "You have run out of time"
    if int(time_left) <= 0:
        end_game(username, reason, chosen_title)
    else:
        return True
        

def typewriter_print(title_string):
    """
    gives typewriter effect when printing the scramled title
    """
    for char in title_string:
        time.sleep(.2)
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


def increase_score(level_choice):
    """
    Increase score by 1, 2 or 3 according to level of difficulty
    """
    global SCORE
    if level_choice == "1":
        SCORE +=1
    elif level_choice == "2":
        SCORE +=2
    elif level_choice == "3":
        SCORE +=3


def loose_a_life():
    """
    Reduce LIVES by 1
    Print remaining lives/life to console
    String guitar
    """
    global LIVES
    LIVES = LIVES -1
    if LIVES == 1:
        print(f"\nYou have {LIVES} Life left\n")
        print(f"{tcolours.blue}{guitar[(LIVES)]}{tcolours.end}")
    else:
        print(f"\nYou have {LIVES} Lives left\n")
        print(f"{tcolours.blue}{guitar[(LIVES)]}{tcolours.end}")



def play_again(username):
    """
    Returns the user to the level choice section if yes
    or the Intro page if no
    """
    print("Would you like to play again?")
    while True:
        play = input(f"Y for Yes or N for No :\n")
        if play in ("y", "Y"):
            play_game(username)
            break
        elif play in ("n", "N"):         
            update_scores(username, SCORE)
            exit()
            break
        else:
            print(f"{tcolours.red}Incorrect input, please try again Y or N{tcolours.end}")


def update_scores(username, score):
    """
    Update the SCORE bby increasing it by 1 
    each time this function is called
    """
    global SCORE
    global LIVES
    data = [username, score]
    scores_worksheet = SHEET.worksheet('scores')
    scores_worksheet.append_row(data)
    SCORE = 0
    LIVES = 3


def score_board():
    """
    return top 5 scores from spreadsheet
    """
    clear()
    print(f"{tcolours.green}{score_board_banner[0]}{tcolours.end}")
    scores_data = SHEET.worksheet('scores')
    scores_data.sort((2, 'des'))
    i = 0
    while i < 5:
        print(f"\n   {tcolours.mag}{(scores_data.col_values(1)[i])}:  {(scores_data.col_values(2)[i])}{tcolours.end}") 
        i +=1


def reset_lives():
    global LIVES
    LIVES = 3


def end_game(username, reason, chosen_title):
    """
    Game over message, displays reason the game ended no lives or no time left
    Reveals correct answer
    Displays final score
    Upates scores sheet
    Asks the user do they want to play again
    """
    global SCORE
    #print(f"{tcolours.green}{game_over_banner[0]}{tcolours.end}")
    clear()
    print(f"{tcolours.red}Game Over{tcolours.end} - {reason}")
    print(f"{tcolours.blue}{guitar[0]}{tcolours.end}")
    print(f"The correct title was {tcolours.green}{chosen_title}{tcolours.end} ")
    print(f"your final score is {tcolours.green}{SCORE}{tcolours.end}\n")
    update_scores(username, SCORE)
    play_again(username)


def exit():
    score_board()
    print(f"\nEnd Game\n")


def play_game(username):
    reset_lives()
    level_choice = select_level(username)
    titles_to_use = load_words(level_choice)
    chosen_title = random_title(titles_to_use)
    scrambled_title = split_and_scramble(chosen_title)
    load_question(username, scrambled_title, chosen_title, level_choice, guitar)


def main():
    username = get_username()
    play_game(username)


main()



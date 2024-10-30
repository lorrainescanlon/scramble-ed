import gspread
import random
import array
import time
import sys
from google.oauth2.service_account import Credentials
from os import system, name
from random import shuffle
from art import game_title_banner, guitar, score_board_banner, game_over_banner
from colours import colr

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
    print(f"{colr.g}{game_title_banner[0]}{colr.e}")
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
        elif len(name) == 0:
            raise ValueError(
                "Username can not be blank"
            )

    except ValueError as e:
        print(f"\n{colr.r}Invalid data: {e}, please try again.{colr.e}\n")
        return False
    return True


def select_level(username):
    """
    Prompts the user to enter a level of difficulty.
    """
    clear()
    while True:
        print(f"\n")
        print(f"{username} please choose a level of difficulty: 1, 2, or 3\n")
        print("Scores are weighted according to level choice\n")
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
        print(f"\n{colr.r}Invalid data: {e}, please try again.{colr.e}")
        return False
    return True


def load_words(choice):
    """
    Load songs from worksheet column into a list according to level choice
    """
    titles_to_use = []
    songs = SHEET.worksheet('songs')
    titles_to_use = songs.col_values(int(choice))
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


def load_question(username, scrambled_title, chosen_title,
                  level_choice, guitar):
    """
    loads the scrambled title and prompts the player to enter a guess.
    Calls the timer function to set a timer for the game.
    Checks answer, if correct increases score and prompts user to play again.
    If incorrect prompts the user to try again until lives are 0 or time is up.
    """
    clear()
    print(f"\n\nGood Luck {username}, your Scrambled Ed song title is:\n")
    typewriter_print((f"{colr.c}{scrambled_title}{colr.e}"), .2)
    print(f"{colr.b}{(guitar[3])}{colr.e}")
    time_up = set_time()

    global LIVES

    while check_lives(username, chosen_title) and \
            check_time(username, time_up, chosen_title):
        guess = input(f"Your Guess here, or quit to exit:\n")
        if guess == "quit":
            reason = "You Quit"
            end_game(username, reason, chosen_title)
            break
        elif guess == chosen_title:
            print(f"\n{colr.g}Well Done You've guessed it{colr.e}\n")
            increase_score(level_choice)
            play_again(username)
            break
        else:
            clear()
            print(f"\n{colr.r}Wrong guess, please try again{colr.e}\n")
            loose_a_life()
            print(f"Your chosen song title is: {colr.c}{scrambled_title}\
                {colr.e}\n")


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


def typewriter_print(title_string, speed):
    """
    gives typewriter effect when printing to the console
    """
    for char in title_string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

    print(f"\n")


def clear():
    """
    Clears console screen
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def increase_score(level_choice):
    """
    Increase score by 1, 2 or 3 according to level of difficulty
    """
    global SCORE
    if level_choice == "1":
        SCORE += 1
    elif level_choice == "2":
        SCORE += 2
    elif level_choice == "3":
        SCORE += 3


def loose_a_life():
    """
    Reduce LIVES by 1
    Print remaining lives/life to console
    String guitar
    """
    global LIVES
    LIVES = LIVES - 1
    if LIVES == 1:
        print(f"\nYou have {LIVES} Life left\n")
        print(f"{colr.b}{guitar[(LIVES)]}{colr.e}")
    else:
        print(f"\nYou have {LIVES} Lives left\n")
        print(f"{colr.b}{guitar[(LIVES)]}{colr.e}")


def play_again(username):
    """
    Returns the user to the level choice section if yes
    or game over if no
    """
    print("Would you like to play again?")
    while True:
        play = input(f"Y for Yes or N for No :\n")
        if play in ("y", "Y"):
            play_game(username)
            break
        elif play in ("n", "N"):
            exit()
            break
        else:
            print(f"{colr.r}Incorrect input, please try again Y or N{colr.e}")


def update_scores(username, score):
    """
   Write username and score to spreadsheet
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
    print(f"{colr.g}{score_board_banner[0]}{colr.e}")
    scores_data = SHEET.worksheet('scores')
    scores_data.sort((2, 'des'))
    i = 0
    while i < 5:
        print(f" {colr.b}{(scores_data.col_values(1)[i])}:\
          {(scores_data.col_values(2)[i])}{colr.e}")
        print(f"\n")
        i += 1


def reset_lives():
    """
    reset LIVES to 3
    """
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
    clear()
    print(f"{colr.r}Game Over{colr.e} - {reason}")
    print(f"{colr.b}{guitar[0]}{colr.e}")
    print(f"The correct title was {colr.g}{chosen_title}{colr.e} ")
    print(f"your final score is {colr.g}{SCORE}{colr.e}\n")
    update_scores(username, SCORE)
    play_again(username)


def exit():
    """
    Print Game Over banner and load score board
    """
    clear()
    print(f"\n\n")
    typewriter_print((f"{colr.b}{game_over_banner[0]}{colr.e}"), 0.01)
    time.sleep(1)
    score_board()


def play_game(username):
    """
    Calls functions needed to play game
    """
    reset_lives()
    level_choice = select_level(username)
    titles_to_use = load_words(level_choice)
    chosen_title = random_title(titles_to_use)
    scrambled_title = split_and_scramble(chosen_title)
    load_question(username, scrambled_title, chosen_title, level_choice,
                  guitar)


def main():
    username = get_username()
    play_game(username)


main()

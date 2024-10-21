import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes (SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('edsongs')

songs = SHEET.worksheet('songs')

data = songs.get_all_values()


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

get_username()

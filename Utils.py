import os
import platform

# 1. SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt”
SCORES_FILE_NAME = "Scores.txt"

# 2. BAD_RETURN_CODE - A number representing a bad return code for a function.
BAD_RETURN_CODE = -1

# 3. screen_cleaner - A function to clear the screen
def screen_cleaner():
    """
    Clears the terminal screen.
    
    """
    os.system('cls' if platform.system() == 'Windows' else 'clear')

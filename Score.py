import os
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

def add_score(difficulty):
    """
    Adds score to the score file based on the difficulty.
    Score formula: (difficulty * 3) + 5

    If the file doesn't exist or has invalid content, it will be created/reset with the new score.
    Returns the updated score, or BAD_RETURN_CODE if something went wrong.
    """
    try:
        points_to_add = (difficulty * 3) + 5

        # Read the current score if the file exists
        if os.path.isfile(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as score_file:
                content = score_file.read().strip()
                try:
                    current_score = int(content)
                except ValueError:
                    current_score = 0
        else:
            current_score = 0

        # Add the new points
        new_score = current_score + points_to_add

        # Write back to the file
        with open(SCORES_FILE_NAME, "w") as score_file:
            score_file.write(str(new_score))

        return new_score

    except Exception as e:
        print(f" Error updating score: {e}")
        return BAD_RETURN_CODE

import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        # Generates a random number between 1 and difficulty, inclusive, and saves it to secret_number.
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        # Prompts the user for a number between 1 and difficulty and returns it.
        while True:
            try:
                guess = int(input(f"Guess a number between 1 and {self.difficulty}: "))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print(f"Please enter a number between 1 and {self.difficulty}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def compare_results(self, guess):
        # Compares the user's guess to the secret number.
        if guess == self.secret_number:
            return True
        else:
            return False

    def play(self):
        # Plays the game by generating a number, getting the user's guess, and comparing the results.
        self.generate_number()
        print("Welcome to the Guess Game!")

        while True:
            guess = self.get_guess_from_user()
            if self.compare_results(guess):
                print("Congratulations, you guessed the secret number!")
                return True
            else:
                print("Incorrect guess, try again.")

# Example of playing the game with a difficulty of 10
game = GuessGame(difficulty=10)
game.play()
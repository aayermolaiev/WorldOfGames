import random

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.usd_to_ils_rate = 3.72  # Mocked exchange rate for USD to ILS

    def get_money_interval(self):
        # Fetches the exchange rate (mocked here as a static value) and generates an interval for the guessed value.
        # Simulating fetching the exchange rate for USD to ILS (in a real case, you would use an API here)
        total_value_in_ils = random.randint(1, 100) * self.usd_to_ils_rate
        
        # Calculate the interval based on the difficulty
        margin = 5 - self.difficulty
        lower_bound = total_value_in_ils - margin
        upper_bound = total_value_in_ils + margin
        
        return lower_bound, upper_bound, total_value_in_ils

    def get_guess_from_user(self):
        # Prompts the user to enter their guess for the exchange rate of the generated USD amount.
        while True:
            try:
                guess = float(input("Guess the value of the generated USD amount in ILS: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play(self):
        # Runs the game by calling the other methods and determines if the user wins or loses.
        print("Welcome to Currency Roulette Game!")
        
        # Get the money interval and the correct answer
        lower_bound, upper_bound, correct_value = self.get_money_interval()
        
        # Display the valid guess interval
        print(f"The correct value is between {lower_bound:.2f} and {upper_bound:.2f} ILS.")
        
        # Get the user's guess
        user_guess = self.get_guess_from_user()
        
        # Check if the user's guess is within the interval
        if lower_bound <= user_guess <= upper_bound:
            print("Congratulations! You guessed correctly!")
            return True
        else:
            print(f"Sorry, the correct value was {correct_value:.2f} ILS. You lose.")
            return False

# Example of playing the game with a difficulty of 3
game = CurrencyRouletteGame(difficulty=3)
game.play()

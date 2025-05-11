import random
import time

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.sequence = []

    def generate_sequence(self):
        # Generates a list of random numbers between 1 and 101. The list length will be the difficulty.
        self.sequence = [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        # Prompts the user to input a list of numbers. The list length will be the size of difficulty.
        user_input = []
        print(f"Enter {self.difficulty} numbers:")
        for _ in range(self.difficulty):
            while True:
                try:
                    num = int(input(f"Enter a number: "))
                    user_input.append(num)
                    break
                except ValueError:
                    print("Please enter a valid number.")
        return user_input

    def is_list_equal(self, list1, list2):
        # Compares two lists. Returns True if they are equal, otherwise False.
        return list1 == list2

    def play(self):
        # Plays the memory game. Displays a sequence, then asks for user input, and compares the results.
        print("Welcome to the Memory Game!")
        self.generate_sequence()
        
        # Show the sequence for 0.7 seconds
        print("Remember this sequence of numbers:")
        print(self.sequence)
        time.sleep(0.7)
        
        # Clear the sequence from the display
        print("\033c", end="")  # ANSI escape sequence to clear the terminal screen

        # Get the user's input
        user_sequence = self.get_list_from_user()
        
        # Compare the sequences
        if self.is_list_equal(self.sequence, user_sequence):
            print("Congratulations! You remembered the sequence correctly!")
            return True
        else:
            print("Sorry! You didn't remember the sequence correctly. You lose.")
            return False

# Example of playing the game with a difficulty of 5
game = MemoryGame(difficulty=5)
game.play()

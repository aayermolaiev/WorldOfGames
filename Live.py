from GuessGame import play as play_guess
from MemoryGame import play as play_memory
from CurrencyRulleteGame import play as play_currency
from Score import add_score
from Utils import screen_cleaner

def load_game():
    print(
        "Please choose a game to play:\n"
        "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
        "2. Guess Game - guess a number and see if you chose like the computer\n"
        "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
    ) 

    while True:
        try:
            game = int(input("Please choose a game to play: "))
            if game in [1, 2, 3]:
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    game_names = {1: "Memory Game", 2: "Guess Game", 3: "Currency Roulette"}
    print(f"You chose: {game_names[game]}")

    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if difficulty in [1, 2, 3, 4, 5]:
                break
            else:
                print("Invalid choice. Please select a difficulty between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    game_difficulty = {1: "Very Easy", 2: "Easy", 3: "Normal", 4: "Hard", 5: "Nightmare"}
    print(f"You chose: {game_difficulty[difficulty]}")
    
    screen_cleaner()

    # Play the selected game and store result
    result = False
    if game == 1:
        result = play_memory(difficulty)
    elif game == 2:
        result = play_guess(difficulty)
    elif game == 3:
        result = play_currency(difficulty)

    # Check result and update score if needed
    if result:
        print("You won!")
        add_score(difficulty)
    else:
        print("You lost. Try again!")
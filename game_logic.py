import random
from ascii_art import STAGES
from colorama import init, Back, Fore, Style
init(autoreset=True)


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman stage for the current number of mistakes."""
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(Fore.BLUE + "Word: ", display_word)
    print("\n")


def play_game():
    """Main game loop."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while mistakes < 3:
        # Display the current game state.
        display_game_state(mistakes, secret_word, guessed_letters)

        # Prompt the user for a guess.
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print(f"Wrong guess! You have {3 - mistakes} attempts left.")

            if 3 - mistakes == 0:
                display_game_state(mistakes, secret_word, guessed_letters)
                print("Game Over! You did not save the snowman :( The word was:", secret_word)
                print()
                break

        if set(secret_word).issubset(set(guessed_letters)):
            display_game_state(mistakes, secret_word, guessed_letters)
            print(Back.YELLOW + "Congratulations! You saved the snowman!" + Style.RESET_ALL + " " + Fore.GREEN + "The word was:", secret_word)
            print()
            break






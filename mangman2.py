'''
This code is the recreation of the hangman game. The code is split into severeral different parts.
The first part is the dictionary that contains all the words for the game.
Then a function to pick a word from the list to guess, a fucntion to create the game
establishing the variabless, creating the input to guess, drawing the hangman,
a fucntion for game over, and a fucntion to play the game.
'''

import random

# Dictionary for the computer to choose words from (now with categories)
word_categories = {
    "animals": {
        "dog", "cat", "fish", "bird", "horse"
    },
    "objects": {
        "book", "lamp", "chair", "table", "clock"
    },
    "actions": {
        "play", "jump", "run", "read", "write"
    }
}

# Using random.choice to pick a word from the dictionary
def select_word(categories):
    print("Choose a category:")
    for category in categories:
        print("-", category)

    while True:
        choice = input("Enter a category: ").lower()
        if choice in categories:
            return random.choice(list(categories[choice]))
        else:
            print("Invalid category. Try again.")

# create the game
def create_game(word):
    # Best amount of lives for a reasonable probability
    lives = 6
    blank_space = ["_"] * len(word)
    # Use an empty list to append 
    guessed_letters = []
    return lives, blank_space, guessed_letters

# Function to create input to guess, now with validation
def player_guesses():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please guess only one letter.")
        elif not guess.isalpha():
            print("Please guess a letter, not a number or symbol.")
        else:
            return guess

# Function with ASCII art to create drawings, increasing order of body parts
def draw_hangman(lives):
    hangman_stages = [
        """
          ------
          |    |
               |
               |
               |
               |
        --------
        """,
        """
          ------
          |    |
          O    |
               |
               |
               |
        --------
        """,
        """
          ------
          |    |
          O    |
          |    |
               |
               |
        --------
        """,
        """
          ------
          |    |
          O    |
         /|    |
               |
               |
        --------
        """,
        """
          ------
          |    |
          O    |
         /|\\   |
               |
               |
        --------
        """,
        """
          ------
          |    |
          O    |
         /|\\   |
         /     |
               |
        --------
        """,
        """
          ------
          |    |
          O    |
         /|\\   |
         / \\   |
               |
        --------
        """
    ]

    print(hangman_stages[6 - lives])

# Function for game over
def game_over(blank_space, lives):
    # Conditional statement \
    if "_" not in blank_space:
        print("Yay you guessed the word!")
        return True
]
    if lives <= 0:
        print("\n")
        print("Game over! You ran out of lives.")
        return True
    return False

]
def play_hangman():
    word = select_word(word_categories)
    lives, blank_space, guessed_letters = create_game(word)

    print("Welcome to Mangman")
    print("Your word:", " ".join(blank_space))

    # Use of while loop for guesses and lives
    while True:
        draw_hangman(lives)
        print("Lives remaining:", lives)

        # Use .join to add
        print("Guessed letters:", ", ".join(guessed_letters))
        print("Word:", " ".join(blank_space))

        guess = player_guesses()

        # Conditional statement if letter repeated
        if guess in guessed_letters:
            print("You already guessed that letter.........")
            continue

        # Append to list that was empty before
        guessed_letters.append(guess)

        # Conditional statement \
        if guess in word:
            print("\nCorrect!")
            for i, letter in enumerate(word):
                if letter == guess:
                    blank_space[i] = guess
        else:
            print("Wrong guess!")
            # Decrease lives
            lives -= 1

        # Show word and break loop
        if game_over(blank_space, lives):
            draw_hangman(lives)
            print(f"The word was: {word}")
            break

# Replay option
while True:
    play_hangman()
    again = input("\nWould you like to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break

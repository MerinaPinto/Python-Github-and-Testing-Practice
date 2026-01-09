'''This code is the recreation of the hangman game. The code is split into severeral different parts. The first part is the dictionary
that contains all the words for the game. Then a function to pick a word from the list to guess, a fucntion to create the game
establishing the variabless, creating the input to guess, drawing the hangman, a fucntion for game over, and a fucntion 
to play the game.  '''



import random

# Dictionary for the computer to choose words from
words = {

    "game", "word", "tree", "book",
    "lamp", "fish", "love", "hope",
    "fire", "blue", "song", "ship",
    "star", "home", "rock", "rain",
    "code", "time", "play", "jump",
    "lump", "name", "love"
}

# Using random.choice to pick a word from the dictionary
def select_word(words):
    return random.choice(list(words))

# Function to create the game
def create_game(word):
    # Best amount of lives for a reasonable probability
    lives = 6  
    blank_space = ["_"] * len(word)
    # Use an empty list to append later
    guessed_letters = []
    return lives, blank_space, guessed_letters

# Function to create input to guess, use lower to change to lowercase
def player_guesses():
    return input("Guess a letter: ").lower()

# Function with ASCII art to create drawings, in increasing order of body parts
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
        """,  # 6 lives remaining
        """
          ------
          |    |
          O    |
               |
               |
               |
        --------
        """,  # 5 lives
        """
          ------
          |    |
          O    |
          |    |
               |
               |
        --------
        """,  # 4 lives
        """
          ------
          |    |
          O    |
         /|    |
               |
               |
        --------
        """,  # 3 lives
        """
          ------
          |    |
          O    |
         /|\   |
               |
               |
        --------
        """,  # 2 lives
        """
          ------
          |    |
          O    |
         /|\   |
         /     |
               |
        --------
        """,  # 1 life
        """
          ------
          |    |
          O    |
         /|\   |
         / \   |
               |
        --------
        """,  # 0 lives, GAME OVER
    ]

    print(hangman_stages[6 - lives])

# Function for game over
def game_over(blank_space, lives):
    # Conditional statement to show if word guessed
    if "_" not in blank_space:
        print("Yay you guessed the word!")
        return True
    # Conditional statement of lives = 0 then game over
    if lives <= 0:
        print("\n")
        print("Game over! You ran out of lives.")
        return True
    return False

# Function to play the game
def play_hangman(words):
    word = select_word(words)  # Select a random word
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

        # Conditional statement and enumerate if guessed letter in word
        if guess in word:
            print("\n")
            print("Correct!")
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

play_hangman(words)
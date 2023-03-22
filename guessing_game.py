"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    
    number_to_guess = random.randint(1,10)
    number_of_tries = 1
    current_high_score = 'none!'
    
    print("\n<<<================================>>>",
    "\n***Welcome to Number Guessing Game!***",
    "\n<<<================================>>>\n")


    
    print(f'The current high score is: {current_high_score}')
    
    

    while True:
        try:
            guess_input = input('Guess the number between 1 and 10:\n')
            if not guess_input.isnumeric():
                raise ValueError('Please only enter numbers, characters like "." and "-" are not valid.\n')
        except ValueError as error:
            number_of_tries += 1
            print(f"{error}")
        else:
            try:
                guess = int(guess_input)
                if guess < 1 or guess > 10:
                    raise Exception('This number is outside the range. Please try again.\n')
            except Exception as error:
                number_of_tries += 1
                print(f"{error}")
            else:
                if guess == number_to_guess:
                    print(f"\nYou got it! \n\nThe number of attempts to get it was: {number_of_tries} \n\nThank you for playing! \n")
                    play_again = input('Would you like to play again? Enter Y to play again: ')
                    if play_again.lower() == 'y':
                        number_to_guess = random.randint(1,10)
                        
                        # updates current high score if applicable
                        if current_high_score == 'none!':
                            current_high_score = number_of_tries

                        elif number_of_tries < current_high_score:
                            current_high_score = number_of_tries

                        number_of_tries = 1
                        print(f'\nThe current high score is: {current_high_score}\n')
                        continue                        
                        
                    else:
                        print('\nGoodbye!')
                        exit()
                elif guess > number_to_guess:
                    number_of_tries += 1
                    print("It's lower!")
                elif guess < number_to_guess:
                    number_of_tries += 1
                    print("It's higher!")


# Kick off the program by calling the start_game function.
start_game()
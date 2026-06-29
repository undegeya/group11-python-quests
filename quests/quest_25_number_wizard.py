# Quest 25: The Number Wizard

# WHAT: Setting a fixed secret number for the game
# WHY: The program needs a target value to compare user guesses against
secret_number = 7

print("Welcome to the Number Wizard game!")

# WHAT: Starting an infinite while loop
# WHY: We want the game to keep running until the user guesses correctly
while True:
    # WHAT: Taking input and converting it to an integer
    # WHY: input() always returns text, but we need a number to do math/logic comparisons
    guess = int(input("Guess a number: "))
    
    # WHAT: Comparing if the guess is perfectly correct
    # WHY: If it matches, the game is won, and we use 'break' to terminate the loop
    if guess == secret_number:
        print("Spot on! You guessed it!")
        break
    # WHAT: Checking if the guess is higher than the secret number
    # WHY: Gives specific feedback to help the user adjust their next guess downward
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    # WHAT: Checking if the guess is lower than the secret number
    # WHY: Gives specific feedback to help the user adjust their next guess upward
    else:
        print("Too low! Try a higher number.")
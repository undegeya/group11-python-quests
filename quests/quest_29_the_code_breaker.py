# Quest 29: The Code Breaker

secret_code = "42"

# WHAT: Setting an tracking counter for attempts
# WHY: We need to limit the loop to a maximum of 3 turns
attempts = 0
max_attempts = 3

print("Security System: You must enter the correct code to advance.")

# WHAT: Running a while loop that keeps checking the condition
# WHY: Ensures the loop stops automatically if the user runs out of attempts
while attempts < max_attempts:
    guess = input("Enter code: ").strip()
    attempts += 1 # Adds 1 to the count after every try
    
    # WHAT: Checking if the guess matches the secret code
    # WHY: Breaks the loop immediately upon success so they don't get asked again
    if guess == secret_code:
        print("You may go through ahead!")
        break
    else:
        # WHAT: Giving failure feedback and showing remaining attempts left
        # WHY: Keeps user informed of game state per rules
        remaining = max_attempts - attempts
        print(f"Incorrect. Remaining attempts: {remaining}")

if guess != secret_code:
    print("Wrong code. You may not go through. initiating SYSTEM LOCKDOWN immediately.")
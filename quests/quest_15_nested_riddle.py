# Quest 15: The Nested Riddle
# Concept: Nested if statements

path = input("Do you go 'left' or 'right'? ").lower()

if path == "left":
    action = input("Do you 'swim' or 'wait'? ").lower()
    if action == "swim":
        print("You found a hidden treasure chest!")
    else:
        print("You waited too long and missed your chance.")
else:
    print("You wandered into the forest and got lost.")

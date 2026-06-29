# Quest 28: The Adventure Begins

# WHAT: Defining a function for the clearing pathway
# WHY: Isolates this part of the map/game text structure
def start_adventure():
    print("You stand in a dark forest. There is a path to the 'left' and a path to the 'right'.")
    choice = input("Which way do you go? ").strip().lower()
    
    if choice == "left":
        lake_path()
    elif choice == "right":
        cave_path()
    else:
        print("Confused, you accomplish nothing. Game Over.")

def lake_path():
    print("\nYou reach a peaceful lake. Do you want to 'swim' or 'rest'?")
    choice = input("> ").strip().lower()
    if choice == "swim":
        print("YOU HAVE BEEN DEVOURED BY A SEA KING! You lost...")
    else:
        print("YOU FOUND A TREASURE CHEST! You won!!!")

def cave_path():
    print("\nYou find a creepy cave. Do you enter 'yes' or 'no'?")
    choice = input("> ").strip().lower()
    if choice == "yes":
        print("A dragon wakes up and roasts you alive! Fatality!!!")
    else:
        print("You get back home safely. You have survived... for now")

# Start the game
start_adventure()
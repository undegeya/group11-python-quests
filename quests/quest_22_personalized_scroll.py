# Quest 22: returning value of paraments

def personalized_greeting(name, quest):
    print(f"Hello {name}!")
    print(f"Good luck on your quest: {quest}!")


name = input("Enter your name: ")
quest = input("Enter your quest: ")

personalized_greeting(name, quest)
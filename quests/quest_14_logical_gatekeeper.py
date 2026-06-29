# Quest 14: The Logical Gatekeeper
# Concept: Logical Operators (and, or, not)

age = int(input("Enter your age: "))
gold = int(input("Enter your gold coins: "))

if age >= 18 and gold >= 20:
    print("Welcome! You may enter the club.")
else:
    print("Sorry, you cannot enter. You need to be 18+ and have 20+ gold.")

# Quest 24: Returning age aligible to vote

def ask_for_age():
    age = int(input("Enter your age: "))
    return age


def can_vote(age):
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")


age = ask_for_age()
can_vote(age)
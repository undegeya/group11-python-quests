# Quest 26: The Simple Calculator

# WHAT: Defining individual functions for math operations
# WHY: Functions allow us to organize and isolate calculations cleanly
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("Welcome to the Simple Calculator!")

# WHAT: Collecting numeric values from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Operations: add, subtract")
operation = input("Choose an operation: ").strip().lower()

# WHAT: Using an if-elif-else chain to route the chosen operation
# WHY: Matches user input string to the correct math function execution
if operation == "add":
    result = add(num1, num2)
    print(f"Result: {result}")
elif operation == "subtract":
    result = subtract(num1, num2)
    print(f"Result: {result}")
else:
    print("Invalid operation selected.")
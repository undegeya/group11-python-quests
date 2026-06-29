# Quest 27: The FizzBuzz Test

# WHAT: Using a for loop with range(1, 101)
# WHY: range(1, 101) includes 1 but stops before 101, letting us count exactly from 1 to 100
for i in range(1, 101):
    
    # WHAT: Checking if 'i' is divisible by both 3 AND 5 using the modulo operator (%)
    # WHY: If a number leaves a remainder of 0 when divided by 3 and 5, it's a multiple of both. 
    # This check MUST come first, otherwise standalone 3 or 5 checks would catch it first!
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        
    # WHAT: Checking if 'i' is divisible by 3
    elif i % 3 == 0:
        print("Fizz")
        
    # WHAT: Checking if 'i' is divisible by 5
    elif i % 5 == 0:
        print("Buzz")
        
    # WHAT: Printing the number itself if none of the rules above apply
    else:
        print(i)
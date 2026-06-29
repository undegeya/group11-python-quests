# Total gold and number of friends
gold = 27
friends = 4

# Calculate equal shares and remainder
gold_per_friend = gold // friends
goblin_keeps = gold % friends

# Display the results
print(f"Each friend gets {gold_per_friend} gold pieces.")
print(f"The goblin keeps {goblin_keeps} gold piece(s).")
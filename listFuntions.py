luckyNumbers = [4, 8, 15, 16, 23, 42] # list of numbers (integers) (no quotes)
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"] # list of strings (no quotes)

friends.sort() # Sorts the friends list in alphabetical order
print(friends) # Prints the entire list

friends.extend(luckyNumbers) # Adds the luckyNumbers list to the friends list

print(friends) # Prints the entire list

friends.append("Creed") # Adds "Creed" to the end of the friends list

print(friends) # Prints the entire list

friends.insert(1, "Kelly") # Adds "Kelly" to the second position in the friends list

print(friends) # Prints the entire list

friends.remove("Kelly") # Removes "Jim" from the friends list

print(friends) # Prints the entire list

friends.pop() # Removes the last item from the friends list

print(friends) # Prints the entire list

print(friends.index("Oscar")) # Returns the index of "Kevin" in the friends list

print(friends) # Prints the entire list

print(friends.count("Jim")) # Returns the number of times "Jim" appears in the friends list

print(friends) # Prints the entire list

luckyNumbers.sort() # Sorts the luckyNumbers list in numerical order
print(luckyNumbers) # Prints the entire list

luckyNumbers.reverse() # Reverses the order of the luckyNumbers list
print(luckyNumbers) # Prints the entire list

friends2 = friends.copy() # Copies the friends list to the friends2 list
print(friends2) # Prints the entire list
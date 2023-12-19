phrase = "Giraffe Academy"  # String variable
print(phrase.lower())   # .lower() converts all characters to lowercase
print(phrase.upper())   # .upper() converts all characters to uppercase
print(phrase.isupper()) # .isupper() checks if all characters are uppercase
print(phrase.islower()) # .isupper() checks if all characters are lowercase
print(phrase.upper().isupper()) # .upper() converts all characters to uppercase, then .isupper() checks if all characters are uppercase (True)
print(len(phrase))  # len() returns the length of the string
print(phrase[8])    # [8] returns the character at index 8
print(phrase.index("Acad")) # .index() returns the index of the first character of the string passed as an argument
print(phrase.index("a"))    # .index() returns the index of the first character of the string passed as an argument
print(phrase.replace("Giraffe", "Elephant")) # .replace() replaces the first string passed as an argument with the second string passed as an argument
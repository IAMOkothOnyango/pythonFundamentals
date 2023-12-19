num1 = input("Enter a number: ") # input() always returns a string (even if the user enters a number)
num2 = input("Enter another number: ") # input() always returns a string (even if the user enters a number)

result = num1 + num2 # concatenation (not addition) because num1 and num2 are strings (not numbers)

print(result) # concatenation (not addition) because num1 and num2 are strings (not numbers)

result2 = int(num1) + int(num2) # addition because num1 and num2 are converted to integers (numbers)

print(result2) # addition because num1 and num2 are converted to integers (numbers)
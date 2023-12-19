secretWord = "giraffe"
guess = ""
guessCount = 0
guessLimit = 3
outOfGuesses = False

while guess != secretWord and not(outOfGuesses): # while guess is not equal to secretWord and not outOfGuesses
    if guessCount < guessLimit: # if guessCount is less than guessLimit (3)
        guess = input("Enter guess: ")
        guessCount += 1 # guessCount = guessCount + 1 (incrementing)
    else:
        outOfGuesses = True

if outOfGuesses:
    print("Out of guesses, you lose!")
else:
    print("You win!")

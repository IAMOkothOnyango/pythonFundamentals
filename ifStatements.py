isMale = False # this is a boolean variable (True or False)
isTall = False # this is a boolean variable (True or False)

if isMale and isTall:
    print("You are a tall male")
elif isMale and not(isTall):
    print("You are a short male")
elif not(isMale) and isTall:
    print("You are not a male, but are tall")
else:
    print("You not male and not tall") # this is the default if none of the above conditions are met
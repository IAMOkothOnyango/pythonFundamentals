import random

feetInMile = 5280
metersInKilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def rollDice(num):
    return random.randint(1, num) # random is a module in python library that has a function called randint that takes two arguments and returns a random integer between them

# Path: modulesAndPip.py
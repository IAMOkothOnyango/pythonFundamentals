try:
    # value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
    print("Hey. You can't divide by zero")
except ValueError as err:
    print(err)
    print("Hey. Invalid Input")
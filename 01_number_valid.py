
valid = False
while not valid:
    try:
        number = int(input("Please enter a number between 1 and 10: "))
        # if number is within range return number
        if number >= 1 and number <= 10:
            print("Your number {}".format(number))
            valid = True
        # output and error messages
        else:
            print("Number out of range")
    except ValueError:
        print("Cannot be blank and only whole numbers")
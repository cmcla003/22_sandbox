valid = False
while not valid:
    try:
        name = input("Enter a name: ")

        if name.isdigit() or name =="":
            print("Cannot be blank or have numbers")
        else:
            print("Stored Name: {} ".format(name))
            valid = True

        # output and error messages
    except ValueError:
        print("Cannot be blank")


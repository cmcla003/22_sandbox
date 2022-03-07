
answer = 0
error = "Please enter a whole number"
print("***Welcome the the times tables quiz ***")
valid = False
while not valid:
    try:
        times_table=int(input("Enter a times table you would like to be tested on: "))
        value = int(input("Enter the maximum value for your times table: "))

        for x in range(1,value+1):
            answer = x * times_table
            try:
                guess=int(input("What is {} x {} = ".format(x,times_table)))

                if guess != answer:
                    print("Incorrect {} x {} = {}".format(x,times_table,answer))
                else:
                    print("Correct {} x {} = {}".format(x,times_table,answer))
            except ValueError:
                print(error)

    except ValueError:
        print(error)



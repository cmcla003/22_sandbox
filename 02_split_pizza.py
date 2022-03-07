
print("***Welcome to Pizza Splitter***")

# ask for number of slices of pizza
number_slices = int(input("What is the total number of pizza slices? "))

# ask for number of people sharing
people = int(input("How many people are sharing? "))

# calcualtes even number of slices and amount left over
slices_each = number_slices//people
remaining_slices = number_slices%people

# prints outcome of calculations
print("Everyone gets {} slices of pizza each".format(slices_each))
print("There will be {} slices left".format(remaining_slices))


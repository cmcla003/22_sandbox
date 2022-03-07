

name= str(input("What is your name? "))
if name.isdigit() or name == "":
        name= str(input("What is your name? Your answer can't be blank or have numbers. "))

try:
    age = int(input("How old are you? "))
except ValueError:
    age = int(input("How old are you? You MUST enter a whole number. "))

icecream = str(input("What is you favourite icecream flavour? "))
if icecream.isdigit() or icecream == "":
        icecream= str(input("What is your favourite icecream? Your answer can't have numbers. "))

animal =input("What is your favourite animal? ")
if animal.isdigit() or animal == "":
        animal = str(input("What is your favourite icecream? Your answer can't have numbers. "))

try:
    pi = float(input("What is pi? Your answer should be to 3 decimal places "))
except ValueError:
    pi = float(input("What is pi? Your answer MUST be to 3 decimal places "))


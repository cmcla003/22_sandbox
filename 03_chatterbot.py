
name = input("What is your name?").lower()

if name == "anakin":
  print("How do you do Anakin!")
else:
  print("Nice name, {}.".format(name))

weather = input("So {}, is it hot or cold where you are today? ".format(name)).upper()
if weather == "COLD":
  print("You must be freezing!")
elif weather == "HOT":
  print("Drink plenty of water")
else:
  print("I can't advise you on that type of weather.")

likes_blue = input("Do you like the colour blue?")
if likes_blue == "Yes":
  print("I like blue too")

print("Have a good day! Bye!")


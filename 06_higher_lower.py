from random import randint

number = randint(1,10)
guess = 3

while guess <= 3:
  try:
    # asks user for a number
    num_guess = int(input("Guess a number between 1 and 10 "))

    # assess if in range
    if num_guess < 1 or num_guess > 10:
      print("Warning: Enter a NUMBER between 1 and 10")
      continue

    # no more guesses
    if guess == 1:
      break

    # tells user higher/lower or correct
    if num_guess < number:
      print("Higher")
      print("You have {} guess left".format(guess))
      guess -= 1

    elif num_guess > number:
      print("Lower")
      print("You have {} guess left".format(guess))
      guess -= 1
    else:
      print("Correct")
      print("You guessed it in {} attempts".format(guess))

  # Error for string/ float/ blank input
  except ValueError:
    print("Warning: Please enter a whole number between 1 and 10")

print("Sorry you have run out of guesses, Goodbye")
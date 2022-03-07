from random import randint

number = randint(1,10)
guesses = 0

while guesses < 3:
  guess = int(input("Guess a number between 1 and 10 "))
  guesses +=1
  print (guesses)

  if guess != number:
    print("Incorrect")
  else:
    print("Correct")
    print("You guessed it in {} attempts".format(guesses))

  if guess != number and guess > 3:
    print("Sorry you have run out of guesses")



#guess the number by user


import random
n=random.randrange(1,10)
print("I have selected a number between 1 and 10. Can you guess it?")

while True:
  try:
    guess=int(input("Enter your guess: "))
    if guess > n:
      print("Too high! Try again.")
    elif guess < n:
      print("Too low! Try again.")
    else:
      print("Congratulations! You guessed the number!")
      break

  except ValueError:
    print("Invalid input. Please enter a valid number.")
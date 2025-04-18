import random

import random

low = 1
high = 10

if low <= high:
    guess = random.randint(low , high)
    print(f"Computer's guess is: {guess}") 

    while True:
      feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").strip().lower()
      if feedback == 'C':
        print("The computer guessed correctly!")
        break
      elif feedback == 'H':
        high = guess - 1
        guess = random.randint(low , high)
        print(f"Computer's guess is: {guess}")
      elif feedback == 'L':
        low = guess + 1
        guess = random.randint(low , high)
        print(f"Computer's guess is: {guess}")

      else:
        print("Invalid!")

if low > high:
    print("The number is not in the range")









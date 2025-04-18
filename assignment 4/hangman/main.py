

#hangman

import random

stages = ['''
    --------
    |      |
    |      O
    |     /|\\
    |     / \\
    |
''', '''
    --------
    |      |
    |      O
    |     /|\\
    |     /
    |
''', '''
    --------
    |      |
    |      O
    |     /|\\
    |
    |
''', '''
    --------
    |      |
    |      O
    |     /|
    |
    |
''', '''
    --------
    |      |
    |      O
    |      |
    |
    |
''', '''
    --------
    |      |
    |      O
    |
    |
    |
''', '''
    --------
    |      |
    |
    |
    |
    |
''']

word_list = ["apple", "banana", "grape", "orange", "mango"]
chosen_word = random.choice(word_list)
word_display = ['_' for _ in chosen_word]
guess_letter = []
lives = len(stages) - 1


print("Welcome to Hangman!")
print("Guess the fruits word.")


while True:
  print("".join(word_display))
  guess = input("Guess a letter: ").lower() #restricted user for lower case
  if not guess.isalpha() or len(guess) != 1:
    print("Invalid input. Please enter a single letter.\n")
    continue
  if guess in guess_letter:
    print(f"You've already guessed {guess}. Try again.\n")
    continue
  guess_letter.append(guess)
  if guess in chosen_word:
    print(f"Good guess! {guess} is in the word")
    for index , letter in enumerate(chosen_word):
      if letter == guess:
        word_display[index] = guess
  else:
    print(f"Sorry, {guess} is not in the word. You lose a life.")
    print(stages[len(stages) - lives -1])
    lives -= 1
    print(f"You have {lives} lives left")

    if lives == 0:
      print(stages[lives])
      print(f"You lose!")
      break

    


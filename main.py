#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import os
import random

def chosen_number():
  number = random.randint(1,100)
  return number

def level(i):
  if i == 'easy':
    return 10
  if i == 'hard':
    return 5
  else:
    print("I'm sorry, I didn't understand witch level you want to play! Say one more time, please.")

def play_again(ans):
  if ans == "y" or ans == "n":
    return ans
  else:
    print("I'm sorry, I didn't understand if you want to play again! Say one more time, please. (y/n) ")




def game():
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  
  #establishing the drawn number
  drawn_number = chosen_number()
  
  #establishing difficulty
  life = 0
  while life != 5 and life != 10:
    life = level(input("Choose a difficulty. Type 'easy' or 'hard': "))
    
  guess = 0
  while guess != drawn_number and life > 0:
    print(f"You have {life} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    if guess < 1 or guess > 100:
      print("This number is out of range, try another one between 1 and 100")
    else:
      life -= 1
      if guess > drawn_number:
        print("Too high")
      elif guess < drawn_number:
        print("Too low.")
      elif life == 0:
        print("You've run out of guesses, you lose.")
      else:
        print(f"You got it! The answer was {guess}")

  repeat = 0
  while repeat != "y" and repeat != "n":
    repeat = play_again(input("Do you want to play again? Answer 'y' for yes ou 'n' for no: "))
  return repeat
  
  

play_game = "y"
while play_game == "y":
  print(logo)
  play_game = game()
  os.system('cls')

input("Thank you very much!")

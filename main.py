# High/Low game
import random
from game_data import data
from art import logo, vs
import os, time

def play():
  is_user_wrong = False
  score = 0

  print(logo)
  
  while not is_user_wrong:
    item_A = []
    item_B = []
    while item_A == item_B:
      item_A = random.choice(data)
      item_B = random.choice(data)
    
    print(f"Compare A: {item_A['name']}, {item_A['description']} from {item_A['country']}.")
    print(vs)
    print(f"Against B: {item_B['name']}, {item_B['description']} from {item_B['country']}.")
    user_answer = input("Who have the most followers? A or B: ").lower()

    if user_answer == "a" and item_A['follower_count'] > item_B['follower_count'] or user_answer == "b" and item_A['follower_count'] < item_B['follower_count']:
      score += 1
      print("Correct!!!")
    else:
      is_user_wrong = True
      print(f"Sorry, that was wrong! final score is {score}")

    time.sleep(2)
    os.system('clear')

play()
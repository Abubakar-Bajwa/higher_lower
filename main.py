from game_data import data
import random
from art import logo, vs
from replit import clear

def account_format(account):
  account_name=account["name"]
  account_descr=account["description"]
  account_country=account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def followers(account):
  followers=account["follower_count"]
  return followers

def check_answers(guess, a_followers, b_followers):
  if a_followers>b_followers:
    return guess=="a"
  else:
    return guess=="b"


print(logo)
score=0
account_b=random.choice(data)
continue_game = True
while continue_game:
  account_a=account_b
  account_b=random.choice(data)
  if account_a == account_b:
    account_b=random.choice(data)
  
  
  print(f"compare A: {account_format(account_a)}")
  print(vs)
  print(f"With B: {account_format(account_b)}")
  
  guess=input("Who has more followers, type 'A' or 'B': ").lower()
  is_correct=check_answers(guess, followers(account_a), followers(account_b))
  clear()
  print(logo)
  
  if is_correct:
    score+=1
    print(f"You're right. score: {score}")
    
    
  else:
    print(f"You got it wrong. Final score: {score}")
    continue_game = False
 
  
  
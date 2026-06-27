import random

# Welcome Text!
print("Welcome to the Number Guessing Game!")
# Random Number Generation
random_number = random.randint(1,100)

# Getting User input and validate
def get_user_input() :
    while True :
      try :
         # User input
         user_guess = int(input("Please Enter the Guessing Number : "))
      except ValueError :
         print("Please Enter the valid Whole Number (1 - 100)")
         continue
        
       # Range Validation
      if 1 <= user_guess <= 100 :
         return user_guess
      else :
         print("Please Enter the Whole number between 1 and 100")
         continue
 
         
# Game Play fun
def game_play (random_number) :     
    user_guess = get_user_input()
    # Game Flow
    if random_number < user_guess :
         print("Your Guess was Big!")
         return False
    elif random_number > user_guess :
         print("Your Guess was Small!")
         return False
    else :
         return True


# Play Attempts
def play_attempts () :
    attempts = 0 
    while attempts < 5 :
         game_play_result = game_play(random_number)
         if game_play_result:
             print("You Win, Your Guess was Correct and the number was ",random_number)
             return
         else :
             attempts +=1

    print("You lose and the Numebr was ",random_number)

play_attempts ()

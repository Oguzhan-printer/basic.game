#Import the random library
import random

#Please create a list containing the three actions of the game.
action_list = ['rock', 'paper', 'scissors']

#Add the code to set the scores of players to 0
player1_score = 0
player2_score = 0
#Add a round_counter that is 0 at the beginning
round_counter = 0

#Please ask the user how many rounds they want to play
total_round = input("How many rounds do you want to play? : ")

#Write a while loop and put the game inside
while True:
   
   #increase round_counter by 1 and print it
   round_counter +=1
   print("Round number:", round_counter)

   #Select a random action for each player
   player1_choice = random.choice(action_list)
   player2_choice = action_list[random.randint(0,2)]

   #Use the print function to print the players choices
   print("Player1:", player1_choice)
   print("Player2:", player2_choice)


   #1 - Tie Condition
   if player1_choice == player2_choice:
      print("Tie! Both player chose same action.")

   #2-Winning Conditions
   #Please add the conditional statements for the remaining combinations 

   #Method 1 elif statements using the and operator

   elif player1_choice == 'paper' and player2_choice == 'rock':
      print("Winner is: Player 1")
      player1_score +=1

   elif player1_choice == 'paper' and player2_choice == 'scissors':
      print("Winner is: Player 2")
      player2_score +=1

   elif player1_choice == 'scissors' and player2_choice == 'rock':
      print("Winner is: Player 2")
      player2_score +=1

   elif player1_choice == 'scissors' and player2_choice == 'paper':
      print("Winner is: Player 1")
      player1_score +=1

   elif player1_choice == 'rock' and player2_choice == 'paper':
      print("Winner is: Player 2")
      player2_score +=1

   elif player1_choice == 'rock' and player2_choice == 'scissors':
      print("Winner is: Player 1")
      player1_score +=1

   #print the score
   print("Score:", "Player1 =",player1_score, "Player2 =",player2_score)     

    #stop the while loop if the round_counter equals the number of total rounds
   if round_counter == int(total_round):
     break
 #Print the outcome of the game by using conditional statements
if player1_score > player2_score:
   print("Player 1 won with score", player1_score, ":", player2_score)
elif player1_score < player2_score:
   print("Player 2 won with score", player1_score, ":", player2_score)
else:
   print("There is no winner, tie.")
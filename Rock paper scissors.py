
#rock, paper, scissors Game

import random

#creating infinte loop for playing a game multiple times
while True:
    #taking input from user
    user_choice= input("Select any one (rock,paper,scissors) : ")
    choices = ['rock',"paper",'scissors']
    
    # Randomly choosing the computer's option
    computer_choice =random.choice(choices)
    
    # Displaying the choices made by the user and the computer
    print(f"You choose {user_choice}, Computer choose {computer_choice} .")
    
    # Checking the outcome of the game
    if user_choice==computer_choice:
        print(f"Both players selected {user_choice}. It`s a Tie !! ")
    elif user_choice == "rock":
        if computer_choice =="scissors":
            print("Rock smashes scissors. You win !")
        else :
            print ("Paper covers rock. You lose")
            
    elif user_choice == "scissors":
        if computer_choice =="paper" :
            print ("Scissors cuts paper! You win!")
        else :
            print ("Rock smashes scissors You lose.")
            
    elif user_choice == "paper":
        if computer_choice == "rock":
            print ("Paper covers rock.You win!")
        else :
            print("Scissors cuts paper.You lose.")
    
    # Asking the user if they want to play again
    play_again =input("Do you wanna play again? (y/n) : ")
    
    # Exiting the loop if the user does not want to play again
    if play_again.lower() != "y":
        break

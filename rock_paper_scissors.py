import random

user_wins = 0
comp_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Rock/Paper/Scissor or Q to quit").lower()

    if user_input == "q":
        break 

    if user_input not in options:
        continue            #does not proceeds further rather continues the loop

    random_number = random.randint(0,2)      
    #rock : 0   paper : 1     scissor : 2 

    comp_pick = options[random_number]         #----------> Important Line

    print("Computer picked ", comp_pick, " .")

    if user_input == comp_pick:
        print("Its a tie")

    elif user_input == "rock" and comp_pick == "scissor" :   #both should be true
        print("YOU WON")
        user_wins += 1
        
    elif user_input == "paper" and comp_pick == "rock":
        print("YOU WON")
        user_wins += 1
        

    elif user_input == "scissor" and comp_pick == "paper":
        print("YOU WON")
        user_wins += 1
        
    else:
        print("YOU LOST")
        comp_wins  += 1


print("You won ", user_wins, " times .")
print("The computer won ", comp_wins, " times .")
print("GoOdByE")
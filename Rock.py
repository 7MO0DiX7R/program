import random
user_score  = 0
computer_score=0

while user_score <3 and computer_score <3:
    computer = random.choice(["rock", "paper", "scissors"])
    user = input("rock, paper or scissors? ")

    print("The computer chose", computer,"and the user chose", user ,".")
    if computer == user:
        print("Same score")
    elif computer== "rock" and user== "paper":
        user_score += 1
    elif computer=="paper" and user=="rock":
        computer_score += 1
    elif computer=="scissors" and user=="papper":
        computer_score += 1
    elif computer== "papper" and user=="scissors":
        user_score += 1
    elif computer=="rock" and user=="scissors":
        computer_score += 1
    elif computer=="scissors" and user=="rock":
        user_score += 1

if computer_score > user_score:
    print("Computer wins with",computer_score,"points")
elif user_score > computer_score:
    print("The user wins with",user_score,"points") 

    
    


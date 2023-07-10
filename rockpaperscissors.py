import random

print('-------Hey! Welcome to my game------- ')
play=input("Do you want to play? ")
if play.lower()=="yes":
    print("Okay! Let's play :)")
else:
    print("You have quit")

user_score=0
computer_score=0

while True:
    user=input("Enter your choice\n (rock,paper,scissors): ")
    choices= ["rock","paper","scissors"]
    computer=random.choice(choices)
    print(f"You chose {user} and computer chose {computer}")

    if user==computer:
        print(f"Both selected {user}")
        print("DRAW! DRAW! DRAW!")
    elif (user=="rock" and computer=="scissors"):
        print("Congrats! you won")
        user_score +=1
    elif (user=="scissors" and computer=="rock"):
        print("Oops! computer won")
        computer_score +=1
    elif (user=="paper" and computer=="rock"):
        print("Congrats! you won")
        user_score +=1
    elif(user=="rock" and computer=="paper"):
        print("Oops! computer won")
        computer_score += 1
    elif(user=="scissors" and computer =="paper"):
        print("Congrats! you won")
        user_score +=1
    elif (user=="paper" and computer=="scissors"):
        print("Oops! computer won")
        computer_score += 1

    cont=input("Do you want to continue? (y/n): ")
    if cont.lower() != "y":
        break
print("\n")
print("You have won " + str(user_score) + " times")
print("Computer have won " + str(computer_score) + " times")

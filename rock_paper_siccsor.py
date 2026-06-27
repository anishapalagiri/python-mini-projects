import random
choices=["rock","paper","scissors"]
user=input("Enter rock,paper or scissors:")
computer=random.choice(choices)
print("you choose:",user)
print("computer choose:",computer) 
if user==computer:
    print("It's a Tie!")
elif(user=="rock" and computer=="scissors") or(user=="paper" and computer=="rock") or (user=="scissors" and computer=="paper"):
    print("You Win!")
else:
    print("Computer Wins!")







    
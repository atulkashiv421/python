'''snake water gun game'''
'''
1 for snake
-1 for water
0 for gun'''

import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
yourdict = {"s":1,"w":-1,"g":0}
reversedict = {1:"snake",-1:"water",0:"gun"}
you = yourdict[youstr]
print(f"You chose{reversedict[you]}\ncomputer chose{reversedict[computer]}")

if computer == you:
    print("Its draw")
else:
    if computer == -1 and you == 1:
        print("You win")
    elif computer==-1 and you == 0:
        print("You loose")
    elif computer == 1 and you == -1:
        print("You loose")
    elif computer==1 and you == 0:
        print("You win")
    elif computer == 0 and you == -1:
        print("You loose")
    elif computer==0 and you == 1:
        print("You loose")
    else:
        print("Somwthing wetn wrong")
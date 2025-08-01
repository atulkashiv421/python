'''game function ina program lets a user play game and reutrn the scores  as an integer you need t read a file hi score.txt whixh is either blank or contain the previous hi score you
need to write a prohram to update the hi score whenever the game function breaks the hi score'''

import random

def game():
    user= random.randint(1,62)
    
    with open("hiscore.txt") as f:
     us_er = f.read()
    if (us_er != ""):
       print(int(user))
    else:
       us_er = 0
    print(f"your score is {user}")

    if (user > int(us_er)):
       with open("hiscore.txt") as f:
                print("New high score! Saving...")
       with open("hiscore.txt", "w") as f:
            f.write(str(user))
    else:
        print("Did not beat the high score.")
game()
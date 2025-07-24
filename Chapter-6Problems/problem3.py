'''spam comment it spam or not'''

p1 = "Take a lot of money"
p2 = "subscribe this"
p3 = "buy this"
p4 = "click this"

input = input("Enter your comment: ")

if(p1 in input or p2 in input or p3 in input or p4 in input ):
    print("This is spam")
else:
    print("This is not a spam")
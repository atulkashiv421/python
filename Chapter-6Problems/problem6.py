'''create grade of student with show his mark'''
user = int(input("Enter your marks: "))
if(user > 90 and user<=100):
    print("Ex grade")
elif( user>80 and user<=90):
    print("A grade")
elif( user>70 and user<=80):
    print("B grade")
elif( user>60 and user<=70):
    print("C grade")
elif( user>50 and user<=60):
    print("D grade")
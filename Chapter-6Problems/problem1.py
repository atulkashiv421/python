# #Write a program to find the greatest of four numbers entered by the user.
a1 = int(input("Enter any number: "))
a2 = int(input("Enter any number:"))
a3 = int(input("Enter any number:"))
a4 = int(input("Enter any number:"))
if(a1>a2 and a1>a3 and a1>a4):
     print("A1 is the laargest no. in those all numbers ",a1)
    
elif(a2>a1 and a2>a3 and a2>a4):
     print("A2 is the laargest no. in those all numbers ",a2)

elif(a3>a1 and a3>a4 and a3>a2):
     print("A3 is the laargest no. in those all numbers ",a3)


else:
     print("A4 is the laargest no. in those all numbers ",a4)


#write a program to find out whether a student has passed or failed it requires a total of 40% and atleast 30# in each subject to pass take only 3 subject and input from user 
mark1 = int(input("Enter first subject marks: "))
mark2 = int(input("Enter second subject marks: "))
mark3 = int(input("Enter third subject marks: "))

total_percent= (100*(mark1+mark2+mark3))/300
print(total_percent)

if(total_percent>40 and mark1>33 and mark2>33 and mark3>33):
    print("You are pass")
else:
    print("You failed,better luck next time")

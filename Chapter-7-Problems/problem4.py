'''prime or not'''
n = int(input("Enter any number: "))
for i in range( 2,n):
    if(n%2)==0:
        print("This is not prime number")
        break
else:
    print("This is prime number")
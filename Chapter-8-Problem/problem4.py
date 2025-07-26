'''sum of first natural n number'''
 #print n natural number
def natural(n):
    if(n == 0):
       return 0
    return n + natural(n-1)
a = int(input("Enter the natural number for sum: "))
print(f"The sum is: {natural(a)}")
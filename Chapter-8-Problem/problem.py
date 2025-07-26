#write a program to find thre greater number
def greater():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    if a>b and a>c :
        print(f"{a}and{b}and{c}greater is : {a}")
    elif b>a and b>c :
        print(f"{a}and{b}and{c}greater is : {b}")
    else :
        print(f"{a}and{b}and{c}greater is : {c}")
greater()
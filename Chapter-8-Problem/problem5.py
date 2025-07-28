'''WAF program for multiplication table of n using for loop in reverse orer'''
a = int(input("enter the number: "))
for i in range(1,11):
    print(f"{a} X {11-i} = {a*(11-i)}")
    
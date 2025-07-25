#write a program ro print multiplication table of a given number using a for loop

table = int(input("Enter the table: "))
for i in range(1,8):
    print(f"{table} X {i} = {table*i}")

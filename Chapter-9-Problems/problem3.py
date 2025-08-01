# "generate table and move in file to save"
def t():
 with open("tables.txt","w") as f:
  for i in range(1, 11):  # i = 1 se 10
    print(f"Table of {i}:\n")
    for j in range(1, 11):  # j = 1 se 10
        table=(f"{i} x {j} = {i * j}")
        print(table)
        f.write(table)
        f.write("\n")
t()
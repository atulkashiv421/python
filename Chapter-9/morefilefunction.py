
# st = f.readlines()
# print(st)
# f.close()

# f = open("Chapter 9/file.txt")
# st = f.read()

# print(st)
# f.close()
f= open("Chapter 9/file.txt")
st = f.readline()
print(st)
line = "Hey atul you are amazing"
while st:
 if (st != line):
    print(st)
    st = f.readline()
    
f.close()

'''with statement'''
with open("Chapter 9/file.txt") as  f:
  print(f.read())


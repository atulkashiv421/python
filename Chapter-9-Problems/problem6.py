'''set the copy of this.txt'''
with open("this.txt") as f:
    d = f.read()
with open("this_save.txt","w") as f:
    f.write(d)
with open("this.txt") as f:
    d = f.read()
with open("rename_at.txt","w") as f:
    f.write(d)
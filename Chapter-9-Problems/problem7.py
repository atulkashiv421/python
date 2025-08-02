'''there are two file and check these file are not same'''

with open("this.txt") as f:
    aa = f.read()

with open("tables.txt") as f:
    asa = f.read()

if (aa == asa) :
    print("Yes these files are identical")
else:
    print("No these are not identical")
'''write a program to greet all the person name stored in a list and strt with s'''
l = ["sharry","soham","rahul","shiv"]
for item in l:
    if(item.startswith("s")):
        print(item)
    else:
        print("done")
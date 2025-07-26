def user(name,ending):
    print("good dAY"+ name + ending)
    return "ok"   
a = user("Atul","thank you")
print(a)

#by default
def user(name , ending = "thank you"):
    print(f"good day, {name}")
    print(ending)
    return("arshit")
a = user("atul")
print(a)

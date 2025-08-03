class demo :
    a = 0#this is class attribute
    print(a)
o = demo()
print(o.a)#this is class attribute bcz there are no present instance attribute
o.a= 7
print(o.a)#this is instance attribute so its change the value but not change attribute
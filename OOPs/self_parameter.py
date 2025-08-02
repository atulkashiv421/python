class Employee:
    name ="Atul"#this is class attribute
    age=24
    def getinfo(self):
        print(f"the name is : {self.name} The age is :{self.age} ")
    def user(self):
        a = 23
        b = 24
        sum= a+b
        print(sum)
    def calc(self):
        list=[]
    
kemon= Employee()
# Employee.getinfo(Atul)
kemon.getinfo()
kemon.user()
'''create a class of programmer to store some information working at micrsoft'''
class programmer():
    company = "Microsoft"
    def __init__(self,name,age,home):
      self.name=name 
      self.age=age
      self.home=home 
p = programmer("Atul",18,"Salouni")
print(p.name,p.age,p.home)
e = programmer("Harry",18,"Salouni")
print(e.name,e.age,e.home)
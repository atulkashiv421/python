
class unknown:
    
    @property
    def person(self):
        return f"{self.fname} {self.lname}"
    @person.setter
    def person(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
e = unknown()
e.person = "Atul kashiv"
print(e.person)


     

class maxe:
    def __init__(self,number):
       self.number=number
    def fi(self):
       if self.number:
           return (max(self.number))
       else:
           return ("This list empty")


finder = maxe([1,2,3,4,5,6])
print(f"The largest number is: ",finder.fi())

           

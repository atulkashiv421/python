'''class "calculator capable of findinfg square , cube and square root of a number"'''

class calculator :
    def __init__(self,n):
        self.n=n
    def squareroot(self):
        print(f"The sq root of this number is: {self.n*self.n}")
    def cube(self):
        print(f"The cube is: {self.n*self.n*self.n}")
m = calculator(4)
m.squareroot()
m.cube()
        
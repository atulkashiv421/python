
class calculator :
    def __init__(self,n):
        self.n=n
    def squareroot(self):
        print(f"The sq root of this number is: {self.n*self.n}")
    def cube(self):
        print(f"The cube is: {self.n*self.n*self.n}")
    @staticmethod
    def greet():
        print("Hello world")
    
k = int(input("Enter the number:"))
print(f"Answer is: {k*k}")
m = calculator(4)
m.squareroot()
m.cube()
m.greet()
class str:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def det(self):
        print(f"({self.x},{self.y},{self.z})")
    def __str__(self):
         return (f"{self.x}i + {self.y}j + {self.z}k")
k =str(2,3,4)

print(k)
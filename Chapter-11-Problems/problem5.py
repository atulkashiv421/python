class vector:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def vec(self,other):
        return (self.x*other.x) + (self.y*other.y) + (self.z*other.z)
    
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def cro(self,other):
       cx = self.y *self.z-self.z*other.y
       cy = self.z*self.x-self.x*self.z
       cz = self.x*self.y-self.y*self.x
       return vector(cx,cy,cz)
    
    def __str__(self):
       return f"{self.x} + {self.y} + {self.z}"
    def __str__(self):
       return f"({self.x},{self.y},{self.z})"
    
       
v1 = vector(2,3,4)
v2 = vector(3,5,4)
       
v3 = vector(2,3,4)
v4 = vector(3,5,4)
print("Cross product is:",v3.cro(v4))
print("Dot product is: ",v1.vec(v2))



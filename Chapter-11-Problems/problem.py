class Twodvectorz:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        print(f"{self.i}i {self.j}j")

class Thirdvector(Twodvectorz):
    def __init__(self,k):
        super().__init__(2,6)
        self.k=k
        
        print(f"{self.i}i {self.j} j{self.k}k")
f= Thirdvector("3")


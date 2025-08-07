class un:
    def __init__(self,n):
       self.n=n
    def __add__(self,un):
     return self.n + un.n
    

n = un(1)
m = un(2)
print(n+m)

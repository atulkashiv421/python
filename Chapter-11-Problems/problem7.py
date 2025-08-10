class series:
    def total(self,n,a=1,d=2):
        return n*(2*a+(n-1)*d)//2
s = series()
print(s.total(5))
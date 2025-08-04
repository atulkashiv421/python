class name:
    def num(self):
        self.company="infotech"
class hom:
    home="India"
    def __init__(self):
        print(f"Your home is:{self.home}")


class real(name,hom):
    def nu(self):
        self.company="info"

c = name()
v=real()

v.nu()
c.num()

print(c.company,v.company)
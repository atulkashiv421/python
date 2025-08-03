'''train whuich is chekc book ticket'''

class train:
    list=["sunday",'monday']
    @staticmethod
    def day():
        da = input("Enter your day:")
        if  da.lower() in train.list:
            print("Yes there are some ticket left ")
            
        else:
            print("NO seats left")
            return 
    def confirm(self,seats):
       self.seats=seats
       print(f"There are only {seats} seats left")
    @staticmethod
    def sallot():
       en = int(input("Enter your seat for reservation: "))
       print(f"Seat no. {en} is reserved for you")    
t = train()   
if t.day():
 t.confirm("10")
t.sallot()

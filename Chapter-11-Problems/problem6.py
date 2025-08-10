"Build a class employee with multiple construction that can initialize an employee object in different ways"

class employee:
    def __init__(self,Department,id,salary,company):
        self.Department=Department
        self.id=id
        self.salary=salary
        self.company=company
    def detail(self):
        print(f"Department: {self.Department}")
        if self.id:
            print(f"Id: {self.id}")
        if self.salary:
            print(f"Salary: {self.salary}")
        if self.company:
            print(f"Company: {self.company}")

e = employee("cse","123","12000","msc")
e.detail()
    
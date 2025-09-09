class employee():
    company = "Itc"
    def  show(self):
        print(f"the name of the employee is{self.name} and the salry is {self.salary}")

class programmer(employee):
    company = "itc infotech"
    def showlanguage(self):
        print(f"the name is {self.name} and he is good with{self.language}")

a = employee()
b = programmer()
print(a.company,b.company)
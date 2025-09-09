class employee():
    company = "Itc"
    name = "Anu"
    def  show(self):
        print(f"the name of the employee is{self.name} and the company is {self.company}")

class coder():
    language = "python"
    def printlanguage(self):
        print(f"out of all the language here is your language : {self.language}")

class programmer(employee,coder):
    company = "itc infotech"
    def showlanguage(self):
        print(f"the name is {self.name} and he is good with{self.language}")

a = employee()
b = programmer()


b.show()
b.printlanguage()
b.showlanguage()



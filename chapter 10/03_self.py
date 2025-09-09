class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


anu = Employee()
# anu.language = "JavaScript" # This is an instance attribute
anu.greet()
anu.getInfo() 
# Employee.getInfo(anu)
 
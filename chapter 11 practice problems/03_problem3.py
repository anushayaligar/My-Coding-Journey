#Create a class ‘Employee’ and add salary and increment properties to it.
class Employee():
    salary = 234
    incremment = 20
    #Write a method ‘salaryAfterIncrement’ method with a @property decorator
    @property #if we write anything using property we can return anything
    def salaryAfterincreement(self):
        return (self.salary + self.salary * (self.incremment/100))

    # with a setter which changes the value of increment based on the salary.
    @salaryAfterincreement.setter
    def salaryAfterincreement(self,salary):
        self.incremment = ((salary/self.salary-1)*100)



e = Employee()

#a setter which changes the value of increment based on the salary.
e.salaryAfterincreement = 280.8
print(e.incremment)
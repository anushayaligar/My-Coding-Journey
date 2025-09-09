class employee:
    a = 1
    def show(self):
        print(f"the class attribute is : {self.a}")

e = employee()
e.a = 45

e.show()#the output is 45 
# we we want an class attribute to execute rather than the instance attribute the we ahve to use @classmethod like we used static method
class employee:
 a = 1
 @classmethod
 def show(cls):
        print(f"the class attribute is : {cls.a}")

e = employee()
e.a = 45

e.show()# now it will show the 1 as the output
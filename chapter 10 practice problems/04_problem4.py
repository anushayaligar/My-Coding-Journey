# Add a static method in problem 2, to greet the user with hello.

class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the square of an nob is: {self.n*self.n}")
      
    def cube(self):
        print(f"the cube of an nob is: {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"the squarerootof an nob is: {self.n**1/2}")
@staticmethod  #not use the self-parameter
def greet():
    print("hello anu")


a = calculator(4)
a,greet()
a.square()    
a.cube()
a.squareroot()
 
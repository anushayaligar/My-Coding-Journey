# Write a class “Calculator” capable of finding square, cube and square root of a number.
class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the square of an nob is: {self.n*self.n}")
      
    def cube(self):
        print(f"the cube of an nob is: {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"the squarerootof an nob is: {self.n**1/2}")
a = calculator(4)
a.square()    
a.cube()
a.squareroot()   
# Write a class ‘Complex’ to represent complex numbers, 
# along with overloaded operators ‘+’ and ‘*’
# which adds and multiplies them.

class complex():
    def __init__(self,r,i):
        self.r = r
        self.i = i
    # here comes the dunder method
    # These methods allow you to define how your objects behave 
    # with operators, built-in functions, or common Python syntax.

    def __add__(self,c2):
        return complex(self.r + c2.r , self.i + c2.i)
    # showing the answer as this  0x0000016A936D4CD0> that is why str will  comes into picture 
    def __str__(self):
     return f"{self.r}+{self.i}i"
    # now the answer comes in complex form 4 + 6i

    #  now for multiflication 

    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i   # ac - bd
        imag = self.r * c2.i + self.i * c2.r   # ad + bc
        return complex(real, imag)

    # To print the result in proper form
    def __str__(self):
        return f"{self.r}+{self.i}i" if self.i >= 0 else f"{self.r}{self.i}i"

c1 = complex(1,2)
c2 = complex(3,4)
print(c1+c2)
print(c1*c2)
        
           
# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class twoD_vector():
    def __init__(self,i,j):#it is a constructor
        self.i=i
        self.j=j
    def show(self):
     print(f"the vector is {self.i}i + {self.j}j")

class threeD_vector(twoD_vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)# here the i , j will be set 
        self.k=k
    def show(self):
       print(f"the vector is {self.i}i + {self.j}j + {self.k}k")
      

a = twoD_vector(1,2)       
a.show()
b = threeD_vector(1,2,3)
b.show()
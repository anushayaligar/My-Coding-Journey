class employee():
    def __init__(self):
        print("constructor of employee")  
    a = 1

class programmer(employee):
    def __init__(self):
     
     print("constructor of programmer")  
    b = 2
    
class manager(programmer):
    def __init__(self):
     super().__init__()
     print("constructor of manager")  
    c = 3

# o = employee()
# print(o.a)
# print(o.b)# shows an error cause there is no b attribute in the employee

# o = programmer()
# print(o.a,o.b)

o = manager()
print(o.a,o.b,o.c)
# constructor of employee
# 1
# constructor of programmer
# 1 2
# constructor of employee
# 1 2 3
# the output is like this for defferent differnrt if we want programmer constructor   in the manager then we need to include 
# the super().__init__
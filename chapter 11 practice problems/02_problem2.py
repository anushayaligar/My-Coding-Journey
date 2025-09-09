# 2. Create a class ‘Pets’ from a class ‘Animals’ and further 
# create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals():
    pass

class pets(Animals):
    pass

class Dog(pets):
    @staticmethod# no need of self here 
    def bark():
        print("bow bow!")
#   def bark(self):
#      print("bow bow")

#  if we use the static method for above then 
 
d = Dog()
d.bark()
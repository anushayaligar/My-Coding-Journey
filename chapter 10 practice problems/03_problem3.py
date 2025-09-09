# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
class demo:
    a=4

o=demo()
print(o.a)#it prints  4 the class attribute cause the instance attribute is not there
o.a=0#the instance attribute is set
print(o.a)#it prints 0 cause the instance attriburte is present
print(demo.a)#prints class attribute
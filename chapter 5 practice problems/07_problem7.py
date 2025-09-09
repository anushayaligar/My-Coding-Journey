#  can you change the values inside the list which is conatined in the set S
s ={3,6,7 ,8 ,[7,8]}
#No, you cannot change the values inside the list contained in the set S because sets in Python can only contain immutable (unchangeable) objects, and lists are mutable.
S = {3, 6, 7, 8, (7, 8)}  # No error, tuple is immutable
print(S)#The set contains integers (3, 6, 7, 8) and a tuple (7, 8), which is immutable and thus valid in a set.
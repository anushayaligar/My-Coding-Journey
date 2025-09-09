s = { 3,5,76,2,1,5,9}
print(s,type(s))
# methods of set
s.add(566)
print(s,type(s))#order cant be expected here 
s.remove(76)
print(s,type(s))
s.discard(98)
print(s,type(s))#no error even though the 98 is not there in set 
s.pop()
print(s,type(s))
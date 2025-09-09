# what will be the length of following set s
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))# it is showing the length as 2 because here the floating point number 20.0 and 20 are equal
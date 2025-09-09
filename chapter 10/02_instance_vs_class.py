class employee:
    
    lang = "py"# this is class attribute
    salary = 12000
    
anu= employee()
anu.lang= "javascript"# this is an instance attribute
print(anu.salary,anu.lang)


# here in the lang that ie anu.lang that will print the javascript rather than the python because the 
# THE INSTANCE ATTRIBUTE HAVE MORE PRIORITY THAT THE CLASS ATTRIBUTE


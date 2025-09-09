class employee:
    
    lang = "py"# this is class attribute
    salary = 12000
    
anu= employee()
anu.name= "anu"# this is an instance attribute
print(anu.name,anu.salary,anu.lang)

abhi = employee()
abhi.name= "abhi"
print(abhi.name,abhi.lang,abhi.salary)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class


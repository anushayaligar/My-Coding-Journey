# Create a class “Programmer” for storing information of few programmers working at Microsoft./
class programmer:
    company = "Microsoft"
    def __init__(self,name,lang,salary,pin):
        self.name=name
        self.lang=lang
        self.salary=salary
        self.pin=pin
        
p = programmer("anu","py",1200000,123)
print(p.name,p.lang,p.salary,p.pin)
q= programmer("abhi","py",1200000,123)
print(q.name,q.lang,q.salary,q.pin)

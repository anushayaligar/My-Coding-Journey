# Write a python function which converts inches to cms.
def inch_to_cms(inch):
    return inch * 2.54

a = int(input("enter the inch: "))

print(f"the corresponding value in cms is : {inch_to_cms(a)}")
#  if there is a presence of multiple if staetments then will work saparetly with their particular else stetment 
a = int(input("enter the age "))
# if statement 1 
if(a%2 == 0):
    print(" a is even number ")
else:
    print("not even")
# end of if statement 1 
if(a>=18):
    print("you are eligible")
elif(a==0):
    print("hey man you entered zero")
elif(a<0):
    print("Invalid number ")
else:
    print("you are below the age ")


   
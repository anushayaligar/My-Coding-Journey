# Write a program to find whether a given number is prime or not.
# using for loop 

n = int(input("enter the nuber: "))

for i in range(2,n):
    if(n%i)==0:
        print("number is not prime")
        break

else:
        print("number is prime")

        
# using the while loop
n = int(input("enter the nuber: "))

i=2
while(i<n):
    if(n%i)==0:
        print("not prime number")
        break
    i=i+1
else:
    print("prime number")

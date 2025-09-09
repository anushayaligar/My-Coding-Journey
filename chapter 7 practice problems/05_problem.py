# Write a program to find the sum of first n natural numbers using while loop.
n = int(input("enter the number: "))

i= 1
sum = 0
while(i<=n):
    sum += i
    i += 1
   
    print(f"{sum} + {i} = {sum+i}")

    # using for loop 

n = int(input("enter the number: "))

sum = 0 
for i in range(1,n+1):
    sum+=1
    print(f"{sum}+{i}={sum+i}")

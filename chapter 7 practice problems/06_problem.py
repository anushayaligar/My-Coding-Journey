# Write a program to calculate the factorial of a given number using for loop.
# 5! = 1x2x3x4x5

n = int(input("enter the number: "))
product = 1
for i in range(1, n+1):
    product = product * i


print(f"the factorial of {n} is {product}")

#  using while loop 
n = int(input("enter the number: "))
i=1
product=1
while(i<=n):
    product = product*i
    i=i+1
print(f"the factorial of {n} is {product}")
      
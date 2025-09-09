# Write a program to print multiplication table of n using for loops in reversed order.
n = int(input("enter the number: "))

# for i in range(1,11):
#     print(f"{n}*{11-i}={n*(11-i)}")

# for i in range(10, 0, -1):  # Starts from 10 down to 1
#     print(f"{n} x {i} = {n * i}")
i = 10
while (i>=1):
    print(f" {n} * {i} = {n*i}")
    i=i-1
    
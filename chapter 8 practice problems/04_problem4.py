# # Write a recursive function to calculate the sum of first n natural numbers.
# """


# sum(1) = 1 
# sum(2) = 1+2
# sum(3) = 1+2+3
# sum(4) = 1+2+3+4
# sum(5) = 1+2+3+4+5

# sum(n) = 1+2+3+.....n-1+n

# """
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n

# print(sum(4))
# # printing up the numbers from 1 to n
# def up(n):
#     if(n==0):
#         return 
#     up(n-1)
#     print(n)
# a = int(input("enter the n: "))
# up(a)


# # printing down
# def down(n):
#     if(n==0):
#         return 
#     print(n)
#     down(n-1)
# a = int(input("enter the n: "))
# print(down(a))

# # sum of first n natural numbers
# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n

# a = (int(input("enter the number: ")))
# print(sum(a))
# factorial using reccursion 
def fact(n):
    if(n==0):
        return 1
    return (n)*fact(n-1)
a = int(input("enter the value of n: "))
print(fact(a))
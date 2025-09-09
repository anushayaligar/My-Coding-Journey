'''
factorial(1)=1
factorial(2)=2x1
factorial(3)=3x2x1
factorial(4)=4x3x2x1
factorial(5)=5x4x3x2x1

factorial(n)= n*(n-1)

'''

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

n = int(input("enter the number: "))
print(f"The factorial of this number is: ",{factorial(n)})

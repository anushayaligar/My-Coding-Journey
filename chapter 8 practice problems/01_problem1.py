# Write a program using functions to find greatest of three numbers.
def gratest(a,b,c):
    if( a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a= 89
b=34
c=56

print(gratest(a,b,c))
# square of a number
def square(n):
   return n*n

a = int(input("enter the n: "))
print(square(a))
# area ofa circle
def area(r):
    return(3.14* r * r )
a = int (input("enter the r value: "))
print(area(a))
area_circle=area(a)
print(f"the are of circle is = {area_circle}")
#ever or odd
def even_or_odd(n):
    if(n%2==0):
        return "even"
    else:
        return "odd"
a = int (input("enter the n value: "))
print(even_or_odd(a))
#a simple calculator 
def calculator(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Taking inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

print(calculator(num1, num2, op))

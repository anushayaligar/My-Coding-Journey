#  write a program to determine whether the student is passed or failed , if it requires a total of 40% and atleat 33% pecentage of marks in each subjecrt then he will be pass if not he fails 
marks1 = int(input("enter the marks1 "))
marks2 = int(input("enter the marks2 "))
marks3 = int(input("enter the marks3 "))

total_percentage= (((100)*(marks1+ marks2+marks3))/300)

if(total_percentage >=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("CONGRATULATION ! ... you have passed:", total_percentage)
else:
    print("you have failed ", total_percentage )
 
 
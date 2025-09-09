# Read All Lines as List


file = open("example.txt", "r")
# lines = file.readlines()
# print("Lines list:", lines)
# file.close()

# in the form of while 
line = file.readline()
while(line != ""):
    print(line)
    line = file.readline()

file.close()
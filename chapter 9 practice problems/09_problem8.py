# Write a program to find out whether a file is identical & matches the content of another file.
with open("file.txt") as f:
    content = f.read()

with open("file2.txt") as f:
    content2 = f.read

if(content == content2):
    print("yes they are same ")
else:
    print("they are not")
f = open("file.txt")
print(f.read())
f.close()

# the same can be written using the with statement like this

with open("file.txt") as f:
    print(f.read())

    # by using with we dont have to explicitly close the file 
f = open("file.txt")

# lines = f.readlines()

# print((lines), type(lines))

# f.close()

# in while loop form
# what excatly the readlines function is 
# it will read the lines untill we get an empty line like

line = f.readline()
while(line != ""):
  print(line)
  line = f.readline()

f.close()
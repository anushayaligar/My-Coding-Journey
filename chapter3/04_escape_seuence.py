# here ar ethe some escape characters that will help us in the time when we 
# want the new line in the single sentecnce like 
a =" anu is goog girl but\n need some focus "
print(a)
# if you want to build the sting in the another string then 
# a = " anu is good girl and "brilliant "";it will through us error becuse python does not understand where the string is ending so soln is 
a = " anu is good \"girl\" and \"brilliant \""
print(a)

# \n	Newline (moves to the next line)
# \t	Tab (adds a horizontal tab)
# \\	Backslash (inserts a \ character)
# \'	Single quote (used inside single-quoted strings)
# \"	Double quote (used inside double-quoted strings)
# \r	Carriage return
# \b	Backspace
# \f	Form feed
# \v	Vertical tab
# \ooo	Octal value (e.g., \101 for 'A')
# \xhh	Hexadecimal value (e.g., \x41 for 'A')

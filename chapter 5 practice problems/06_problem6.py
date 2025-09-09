# create an empty dict allow 4 friends to enter their favrte language as a value and key as their name assume their names as unique 

d ={}

name = input("enter the freinds name: ")
language = input ("enter the language: ")
d.update({name:language})
name = input("enter the freinds name: ")
language = input ("enter the language: ")
d.update({name:language})
name = input("enter the freinds name: ")
language = input ("enter the language: ")
d.update({name:language})
name = input("enter the freinds name: ")
language = input ("enter the language: ")
d.update({name:language})
print(d)
# 7  if the 2 key that is 2 freinds name is same then what will happen ?
#   it will update wheter you entered the anu for and lang is python then u entered again the anu and js then anu js will be shown and updated
#  8 what if the 2 values are same ?
#  it will okay it will show as we entered 
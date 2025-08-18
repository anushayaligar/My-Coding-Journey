# write a program to fill in the letter template given below with teh name and the date
letter = ''' Dear  <|name|>, 
          you are selected! 
          <|date|> '''
print(letter.replace("<|name|>" , "Anu").replace("<|date|>", "24 april 2025"))
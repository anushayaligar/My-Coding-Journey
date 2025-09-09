# We are going to write a program that generates a 
# random number and asks the user to guess it.
# If the player’s guess is higher than the actual number, 
# the program displays “Lower number please”.
# Similarly, if the user’s guess is too low, the program prints 
# “higher number please” When the user guesses the correct number, 
# the program displays the number of guesses 
# the player used to arrive at the number.import random
import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    a = int(input("enter the guess number: "))
    if(a>n):
        print("lower number please")
        guesses += 1
    elif(a<n):
        print("higher number please")
        guesses += 1
print(f"you have guessed the {n} in {guesses} attempts")

    
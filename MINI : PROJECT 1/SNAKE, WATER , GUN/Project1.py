import random

def game():
    print("Welcome to Snake-Water-Gun Game 🐍💧🔫")
    print("Rules: Snake vs Water -> Snake wins | Snake vs Gun -> Gun wins | Water vs Gun -> Water wins")
    
    choices = ['snake', 'water', 'gun']
    
    user_choice = input("Enter your choice (snake/water/gun): ").lower()
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Tie! 🤝")
    elif (user_choice == 'snake' and computer_choice == 'water') or \
         (user_choice == 'water' and computer_choice == 'gun') or \
         (user_choice == 'gun' and computer_choice == 'snake'):
        print("🎉 You Win!")
    else:
        print("😢 You Lose!")

# Play the game
game()


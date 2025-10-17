def km_to_miles(km):
    return km * 0.621371

def c_to_f(c):
    return (c * 9/5) + 32

def inr_to_usd(inr):
    return inr / 83


while True:
    print("\n===== UNIT CONVERTER =====")
    print("1. Km to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. INR to USD")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        print("Miles:", km_to_miles(km))

    elif choice == "2":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", c_to_f(c))

    elif choice == "3":
        inr = float(input("Enter INR: "))
        print("USD:", inr_to_usd(inr))

    elif choice == "4":
        print("You pressed exit. THANK YOU ")
        break

    else:
        print(" Invalid choice, please enter 1-4.")

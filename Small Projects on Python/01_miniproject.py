while True:
    print("\n===== Simple Calculator =====")
    a = int(input("Enter a number: "))
    b = int(input("Enter a 2nd number: "))
    c = input("Enter your choice (+, -, *, /) or type 'exit' to quit: ")

    if c == "exit":
        print("👋 Exiting... Goodbye!")
        break

    if c == "+":
        print("RESULT:", a + b)
    elif c == "-":
        print("RESULT:", a - b)
    elif c == "*":
        print("RESULT:", a * b)
    elif c == "/":
        if b == 0:
            print("❌ Error: Cannot divide by zero")
        else:
            print("RESULT:", a / b)
    else:
        print("❌ Invalid choice! Please enter +, -, *, / or 'exit'")

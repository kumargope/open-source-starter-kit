import random
import string

def password_generator():
    print("\n--- 🔐 Strong Password Generator ---")
    try:
        length = int(input("Enter password length (e.g., 12): "))
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = "".join(random.choice(chars) for _ in range(length))
        print(f"✅ Your Password: {password}")
    except ValueError:
        print("❌ Please enter a valid number.")

def simple_calculator():
    print("\n--- 🧮 Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+': print(f"Result: {num1 + num2}")
        elif op == '-': print(f"Result: {num1 - num2}")
        elif op == '*': print(f"Result: {num1 * num2}")
        elif op == '/': print(f"Result: {num1 / num2}")
        else: print("❌ Invalid operator")
    except ValueError:
        print("❌ Invalid input.")

def main():
    print("Welcome to the Open Source Starter Kit! 🚀")
    while True:
        print("\nMenu:")
        print("1. Generate Password")
        print("2. Use Calculator")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            password_generator()
        elif choice == '2':
            simple_calculator()
        elif choice == '3':
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
  

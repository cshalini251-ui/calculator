def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero!"
    return n1 / n2

while True:
    print("\nPlease select operation -")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Select operation (1-5): "))

    if choice == 5:
        print("Thank you! Exiting...")
        break

    if choice not in [1, 2, 3, 4]:
        print("Invalid choice! Try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == 2:
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif choice == 3:
        print(f"{num1} * {num2} = {mul(num1, num2)}")
    elif choice == 4:
        print(f"{num1} / {num2} = {div(num1, num2)}")
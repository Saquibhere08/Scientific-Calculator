import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Divide by zero"
def power(x, y): return math.pow(x, y)
def sqrt(x): return math.sqrt(x)
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def tan(x): return math.tan(math.radians(x))
def log(x, base=10): return math.log(x, base)

def menu():
    print("\n--- Scientific Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("10. Log")
    print("0. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == '0':
        print("Exiting calculator.")
        break

    if choice in ['1','2','3','4','5']:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        operations = {
            '1': add,
            '2': subtract,
            '3': multiply,
            '4': divide,
            '5': power
        }

        result = operations[choice](x, y)

    elif choice in ['6','7','8','9','10']:
        x = float(input("Enter number: "))

        if choice == '6':
            result = sqrt(x)
        elif choice == '7':
            result = sin(x)
        elif choice == '8':
            result = cos(x)
        elif choice == '9':
            result = tan(x)
        elif choice == '10':
            base = input("Enter base (default 10): ")
            base = float(base) if base else 10
            result = log(x, base)
    else:
        result = "Invalid choice!"

    print("Result:", result)
